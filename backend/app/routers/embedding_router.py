from fastapi import APIRouter, UploadFile, File
from PIL import Image
from ..services.embedding_service import generate_embedding

router = APIRouter()

@router.post("/embed")
async def embed_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    embedding = generate_embedding(image)
    return {"embedding": embedding}
