import torch
from torchvision import transforms
from PIL import Image
import os
from app.models import AddNet  # Make sure AddNet is defined in models.py

# ----------------- Model Setup -----------------
MODEL_PATH = os.path.join("model", "addnet_model.pth")  # Path to your trained PyTorch model
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Check if model file exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# Instantiate the model
model = AddNet().to(DEVICE)

# Load state_dict if your file contains a state_dict
state_dict = torch.load(MODEL_PATH, map_location=DEVICE)

# Detect whether it's a state_dict or full model
if isinstance(state_dict, dict) and not isinstance(state_dict, torch.nn.Module):
    model.load_state_dict(state_dict)
else:
    model = state_dict  # Already a full model

model.eval()  # Set model to evaluation mode

# ----------------- Image Preprocessing -----------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Adjust size based on your model input
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Standard ImageNet normalization
                         std=[0.229, 0.224, 0.225])
])

# ----------------- Prediction Function -----------------
def predict_mri(image_path: str) -> str:
    """
    Takes an MRI image path, preprocesses it, and returns the predicted Alzheimer's stage.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Open image
    image = Image.open(image_path).convert("RGB")
    
    # Apply transforms and add batch dimension
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    
    # Model inference
    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
    
    # Map prediction to class names
    classes = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
    
    return classes[predicted.item()]
