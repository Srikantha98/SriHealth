import os
import uuid

# ----------------- File Utilities -----------------

def save_upload_file(upload_file, upload_dir="uploads") -> str:
    """
    Save an uploaded file to the uploads directory with a unique filename.
    Returns the saved file path.
    """
    os.makedirs(upload_dir, exist_ok=True)
    # Create unique filename to avoid conflicts
    ext = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_dir, unique_filename)

    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())

    return file_path


def remove_file(file_path: str):
    """
    Delete a file from the system if it exists.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
