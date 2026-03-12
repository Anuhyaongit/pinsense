import torch
import clip
from PIL import Image

print("EmbeddingService loaded")

class EmbeddingService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

    def get_embedding(self, image: Image.Image):
        image_input = self.preprocess(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            embedding = self.model.encode_image(image_input)
        return embedding.cpu().numpy().tolist()
