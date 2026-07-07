from fastapi import FastAPI

from app.api.resume import router as resume_router

app = FastAPI()

app.include_router(resume_router)




@app.get("/")
def home():
    return {"message":"welocome to AI resume screening System"}


