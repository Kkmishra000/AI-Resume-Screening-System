from pathlib import Path
import shutil
import fitz  # PyMuPDF

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_uploaded_file(file):
    file_path = UPLOAD_DIR / file.filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    
    return str(file_path)



def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file using PyMuPDF (fitz).
    
    Args:
        file_path (str): The path to the PDF file.
        
    Returns:
        str: The extracted text from the PDF.
    """
    text = ""
    with fitz.open(file_path) as pdf_document:
        for page in pdf_document:
            text += page.get_text()
    return text    