# app/predict.py
import torch
from PIL import Image
<<<<<<< HEAD
import torchvision.transforms as transforms
from app.model import addnet_model, device, N_CLASSES

# Class names (must match the order used during training)
CLASS_NAMES = ['Mild Dementia', 'Moderate Dementia', 'Non Demented', 'Very mild Dementia']

# -------------------------------
# Preprocessing transforms
# -------------------------------
=======
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
>>>>>>> ce992cb242a545cc31d471593da3d973fe916df1
transform = transforms.Compose([
    transforms.Resize((128, 128)),  # Resize to match model input
    transforms.ToTensor(),           # Convert to tensor
    transforms.Normalize([0.5], [0.5])  # Normalize grayscale image
])

# -------------------------------
# Predict function
# -------------------------------
def predict_mri(file_path: str) -> dict:
    """
    Predicts the Alzheimer stage from a single MRI image.

    Args:
        file_path (str): Path to the MRI image.

    Returns:
        dict: {
            "prediction": str,
            "confidence": float
        }
    """
<<<<<<< HEAD
    # Load image in grayscale
    img = Image.open(file_path).convert("L")
    img = transform(img).unsqueeze(0)  # Add batch dimension
    img = img.to(device)

    # Set model to evaluation mode
    addnet_model.eval()

=======
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Open image
    image = Image.open(image_path).convert("RGB")
    
    # Apply transforms and add batch dimension
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    
>>>>>>> ce992cb242a545cc31d471593da3d973fe916df1
    # Model inference
    with torch.no_grad():
        outputs = addnet_model(img)
        probabilities = torch.softmax(outputs, dim=1).cpu().numpy()[0]
        class_idx = int(probabilities.argmax())
        confidence = float(probabilities[class_idx])

    return {
        "prediction": CLASS_NAMES[class_idx],
        "confidence": round(confidence, 4)
    }
