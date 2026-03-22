from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.embedding_router import router as embedding_router
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(embedding_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend is running!"}

class PinRequest(BaseModel):
    image_url: str

@app.post("/api/submit-pin")
def submit_pin(req: PinRequest):
    print("Received image:", req.image_url)
    return {"status": "ok", "received": req.image_url}
