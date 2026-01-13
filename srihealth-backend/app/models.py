# app/models.py

# ----------------- SQLAlchemy Models -----------------
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)  # optional: link to user
    filename = Column(String, nullable=False)
    predicted_class = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# ----------------- PyTorch CNN Model -----------------
import torch
import torch.nn as nn
import torch.nn.functional as F

class AddNet(nn.Module):
    def __init__(self):
        super(AddNet, self).__init__()
        # CNN layers
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # Fully connected layers
        # Input size after conv+pool layers: 224 -> 112 -> 56 (for each dimension)
        self.fc1 = nn.Linear(32 * 56 * 56, 128)  # adjust based on input image size
        self.fc2 = nn.Linear(128, 4)  # 4 classes for Alzheimer's stages

    def forward(self, x):
        # Convolutional layers with ReLU and pooling
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)

        # Flatten for fully connected layers
        x = x.view(x.size(0), -1)

        # Fully connected layers with ReLU
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
