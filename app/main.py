from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"welocome to AI resume screening System"}


