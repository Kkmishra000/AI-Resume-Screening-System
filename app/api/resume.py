from fastapi import APIRouter,UploadFile, File
from app.services.pdf_services import save_uploaded_file

router = APIRouter()

@router.get("/")
def home():
    return {"message":"welcome to AI resume screening System"}


@router.post("/upload_resume")
def upload_resume(file: UploadFile = File(...)):
    
    file_path = save_uploaded_file(file)
    # Process the uploaded resume file
    # You can save the file, analyze it, or perform any other operations here
    return {"filename": file.filename, "content_type": file.content_type}


