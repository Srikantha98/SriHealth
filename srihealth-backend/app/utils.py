import os
<<<<<<< HEAD
from fastapi import UploadFile
from uuid import uuid4
=======
import uuid
from typing import Optional
>>>>>>> ce992cb242a545cc31d471593da3d973fe916df1

# Directory for temporary MRI uploads
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

<<<<<<< HEAD
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
=======
def save_upload_file(upload_file, upload_dir: str = "uploads") -> str:
    """
    Save an uploaded file to the uploads directory with a unique filename.
    Returns the saved file path.
    
    Args:
        upload_file: File-like object with a `filename` attribute.
        upload_dir: Directory where the file should be saved.
    
    Returns:
        str: Full path of the saved file.
    """
    os.makedirs(upload_dir, exist_ok=True)

    # Extract extension safely
    filename = getattr(upload_file, "filename", None)
    ext = os.path.splitext(filename)[1] if filename else ""
    
    # Create a unique filename to avoid conflicts
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_dir, unique_filename)

    # Write file content
>>>>>>> ce992cb242a545cc31d471593da3d973fe916df1
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    file.file.close()

    return file_path

# -------------------------------
# Delete a file
# -------------------------------
def delete_file(file_path: str):
    """
<<<<<<< HEAD
    Deletes a file from disk if it exists.

    Args:
        file_path (str): Path to the file
=======
    Delete a file from the system if it exists.
    
    Args:
        file_path: Path to the file to be deleted.
>>>>>>> ce992cb242a545cc31d471593da3d973fe916df1
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
