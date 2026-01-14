# app/predict.py
import torch
from PIL import Image
import torchvision.transforms as transforms
from app.model import addnet_model, device, N_CLASSES

# Class names (must match the order used during training)
CLASS_NAMES = ['Mild Dementia', 'Moderate Dementia', 'Non Demented', 'Very mild Dementia']

# -------------------------------
# Preprocessing transforms
# -------------------------------
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
    # Load image in grayscale
    img = Image.open(file_path).convert("L")
    img = transform(img).unsqueeze(0)  # Add batch dimension
    img = img.to(device)

    # Set model to evaluation mode
    addnet_model.eval()

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
