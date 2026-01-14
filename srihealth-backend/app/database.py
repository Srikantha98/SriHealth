from typing import List, Dict
from datetime import datetime

# -------------------------------
# In-memory "database" collections
# -------------------------------

# Stores user info
# Example: {"email": "user@example.com", "password": "hashedpassword", "created_at": datetime}
users_collection: List[Dict] = []

# Stores prediction history
# Example: {"user": "user@example.com", "prediction": "Mild Dementia", "confidence": 0.92, "created_at": datetime}
predictions_collection: List[Dict] = []

# -------------------------------
# Optional helper functions
# -------------------------------

def add_user(email: str, hashed_password: str):
    users_collection.append({
        "email": email,
        "password": hashed_password,
        "created_at": datetime.utcnow()
    })

def find_user(email: str):
    for user in users_collection:
        if user["email"] == email:
            return user
    return None

def add_prediction(user_email: str, prediction: str, confidence: float):
    predictions_collection.append({
        "user": user_email,
        "prediction": prediction,
        "confidence": confidence,
        "created_at": datetime.utcnow()
    })

def get_user_predictions(user_email: str):
    return [p for p in predictions_collection if p["user"] == user_email]
