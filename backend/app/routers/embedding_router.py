from fastapi import APIRouter, UploadFile, File
from PIL import Image
from ..services.embedding_service import EmbeddingService

router = APIRouter()
embedder = EmbeddingService()

@router.post("/embed")
async def embed_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    embedding = embedder.get_embedding(image)
    return {"embedding": embedding}
