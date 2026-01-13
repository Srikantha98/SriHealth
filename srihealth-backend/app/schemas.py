from pydantic import BaseModel, EmailStr

# ----------------- User Schemas -----------------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: str  # ISO datetime string

    class Config:
        orm_mode = True

# ----------------- Auth / Token Schemas -----------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int | None = None

# ----------------- Prediction Schemas -----------------

class PredictionResponse(BaseModel):
    filename: str
    predicted_class: str
    created_at: str

    class Config:
        orm_mode = True
