import torch
from torchvision import transforms
from PIL import Image
import os

# ----------------- Model Setup -----------------
MODEL_PATH = os.path.join("model", "best_model.pth")  # Path to your trained PyTorch model
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the trained model
model = torch.load(MODEL_PATH, map_location=DEVICE)
model.eval()  # Set model to evaluation mode

# Define image preprocessing
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
