from fastapi import APIRouter,UploadFile, File, HTTPException
from app.services.pdf_services import save_uploaded_file , extract_text_from_pdf
from app.database.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.schemas.question import QuestionRequest    
from app.services.text_processing import chunk_text
from app.services.llm_service import generate_answer
from app.services.embedding_service import generate_embeddings
from app.services.embedding_service import model
from app.services.faiss_service import add_embeddings, search_similar_chunks

router = APIRouter(prefix="/resume", tags=["Resume"])

@router.get("/")
def home():
    return {"message":"welcome to AI resume screening System"}


@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    try:
        file_path = save_uploaded_file(file)
        
        extract_text = extract_text_from_pdf(file_path)
        
        chunks = chunk_text(extract_text)
        
        embeddings = generate_embeddings(chunks)
        
        add_embeddings(embeddings,chunks)
        
        resume = Resume(
            name = file.filename,
            pdf_path=file_path, 
            extracted_text=extract_text
        )
        
        db.add(resume)
        db.commit()
        db.refresh(resume)
        
        return {"message": "Resume uploaded and processed successfully.", "resume_id": resume.id}
    except Exception as e:
        db.rollback()
        
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the resume: {str(e)}")
    

@router.post("/ask_question")
async def ask_question(request: QuestionRequest):
    retrieved_chunks = search_similar_chunks(
        request.question,
        model 
    )
    
    answer = generate_answer(retrieved_chunks, request.question)
    
    
    return{
        "question": request.question,
        "answer": answer
    }
    
    