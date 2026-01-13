import os
import uuid
from typing import Optional

# ----------------- File Utilities -----------------

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
    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())

    return file_path


def remove_file(file_path: str):
    """
    Delete a file from the system if it exists.
    
    Args:
        file_path: Path to the file to be deleted.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
