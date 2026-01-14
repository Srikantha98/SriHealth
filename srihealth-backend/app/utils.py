import os
from fastapi import UploadFile
from uuid import uuid4

# Directory for temporary MRI uploads
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -------------------------------
# Save uploaded file
# -------------------------------
def save_uploaded_file(file: UploadFile) -> str:
    """
    Saves an uploaded FastAPI file to the uploads directory.

    Args:
        file (UploadFile): FastAPI uploaded file

    Returns:
        str: Path to saved file
    """
    # Create unique filename
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    file.file.close()

    return file_path

# -------------------------------
# Delete a file
# -------------------------------
def delete_file(file_path: str):
    """
    Deletes a file from disk if it exists.

    Args:
        file_path (str): Path to the file
    """
    if os.path.exists(file_path):
        os.remove(file_path)
