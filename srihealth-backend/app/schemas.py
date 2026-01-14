# app/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

# -------------------------------
# User Registration Request
# -------------------------------
class UserRegister(BaseModel):
    email: EmailStr
    password: str

# -------------------------------
# User Login Request
# -------------------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# -------------------------------
# JWT Token Response
# -------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# -------------------------------
# Prediction Response
# -------------------------------
class PredictionResponse(BaseModel):
    prediction: str
    confidence: float

# -------------------------------
# Prediction History Item
# -------------------------------
class PredictionHistoryItem(BaseModel):
    user: str
    prediction: str
    confidence: float
    created_at: datetime  # datetime object for proper handling
