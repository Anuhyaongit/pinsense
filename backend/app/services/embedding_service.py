from sentence_transformers import SentenceTransformer

model = SentenceTransformer("clip-ViT-B-32")

def generate_embedding(image):
    embedding = model.encode(image)
    return embedding.tolist()
