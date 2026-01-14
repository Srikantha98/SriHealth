# app/model.py
import torch
import torch.nn as nn
import os

# -------------------------------
# Global variables
# -------------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
IMAGE_SIZE = 128
N_CLASSES = 4
MODEL_PATH = os.path.join("model", "addnet_model.pth")  # Make sure this exists

# -------------------------------
# Define AddNet architecture
# -------------------------------
class AddNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc = nn.Sequential(
            nn.Linear(64 * (IMAGE_SIZE // 4) * (IMAGE_SIZE // 4), 128),
            nn.ReLU(),
            nn.Linear(128, N_CLASSES)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)  # Flatten
        return self.fc(x)

# -------------------------------
# Load model function
# -------------------------------
def load_model():
    model = AddNet().to(device)
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval()
    return model

# -------------------------------
# Initialize model globally
# -------------------------------
addnet_model = load_model()
