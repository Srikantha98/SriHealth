# app/main.py
from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os, shutil, uuid

from app.database import SessionLocal, engine, Base
from app import models, schemas, auth, predict

# ----------------- Database Setup -----------------
Base.metadata.create_all(bind=engine)

# ----------------- FastAPI App -----------------
app = FastAPI(
    title="SriHealth Backend API",
    description="API for SriHealth Alzheimer's Disease Prediction System",
    version="1.0.0"
)

# ----------------- CORS -----------------
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- DB Dependency -----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------- Auth Endpoints -----------------
@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user/email exists
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pwd = auth.hash_password(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = auth.create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}

# ----------------- Upload Folder -----------------
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------- Prediction Endpoint -----------------
@app.post("/predict")
def predict_mri_endpoint(file: UploadFile = File(...)):
    """
    Upload an MRI image file and return the predicted Alzheimer's stage.
    """
    try:
        # Generate a unique filename to avoid conflicts
        ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

        # Save uploaded file
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Run prediction
        result = predict.predict_mri(file_path)

        # Optional: Remove file after prediction to save storage
        # os.remove(file_path)

        return {"prediction": result, "filename": unique_filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
