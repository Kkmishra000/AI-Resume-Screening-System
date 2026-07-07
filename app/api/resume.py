from fastapi import APIRouter,UploadFile, File


router = APIRouter()

@router.get("/")
def home():
    return {"message":"welcome to AI resume screening System"}


@router.post("/upload_resume")
def upload_resume(file: UploadFile = File(...)):
    # Process the uploaded resume file
    # You can save the file, analyze it, or perform any other operations here
    return {"filename": file.filename, "content_type": file.content_type}

