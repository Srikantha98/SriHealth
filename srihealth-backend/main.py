# main.py
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List

# -------------------------------
# Import local modules
# -------------------------------
from app.schemas import UserRegister, UserLogin, Token, PredictionResponse, PredictionHistoryItem
from app.auth import hash_password, verify_password, create_access_token, get_current_user
from app.utils import save_uploaded_file, delete_file
from app.predict import predict_mri
from app.database import add_user, find_user, add_prediction, get_user_predictions

# -------------------------------
# Initialize FastAPI
# -------------------------------
app = FastAPI(
    title="SriHealth – Alzheimer Prediction (MongoDB-free)",
    description="Backend for Alzheimer disease prediction using AddNet model",
    version="1.0"
)

# -------------------------------
# Enable CORS (allow all origins for demo purposes)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -------------------------------
# Health Check
# -------------------------------
@app.get("/")
def root():
    return {"status": "Backend running (MongoDB-free mode)"}

# -------------------------------
# User Registration
# -------------------------------
@app.post("/register")
def register(user: UserRegister):
    if find_user(user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed = hash_password(user.password)
    add_user(user.email, hashed)
    
    return {"message": "User registered successfully (in-memory)"}

# -------------------------------
# User Login
# -------------------------------
@app.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = find_user(user.email)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# -------------------------------
# Predict Alzheimer Stage (Protected)
# -------------------------------
@app.post("/predict", response_model=PredictionResponse)
def predict_api(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    # Save the uploaded MRI temporarily
    file_path = save_uploaded_file(file)
    try:
        # Run prediction
        result = predict_mri(file_path)
        
        # Store prediction in in-memory database
        add_prediction(current_user, result["prediction"], result["confidence"])
        
        return PredictionResponse(
            prediction=result["prediction"],
            confidence=result["confidence"]
        )
    finally:
        # Delete temporary file
        delete_file(file_path)

# -------------------------------
# Get User Prediction History
# -------------------------------
@app.get("/history", response_model=List[PredictionHistoryItem])
def prediction_history(current_user: str = Depends(get_current_user)):
    history = get_user_predictions(current_user)
    
    formatted_history = [
        PredictionHistoryItem(
            user=h["user"],
            prediction=h["prediction"],
            confidence=h["confidence"],
            created_at=h["created_at"]
        )
        for h in history
    ]
    return formatted_history
