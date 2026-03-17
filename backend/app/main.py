from fastapi import FastAPI
from .routers.embedding_router import router as embedding_router

app = FastAPI()

app.include_router(embedding_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend is running!"}
