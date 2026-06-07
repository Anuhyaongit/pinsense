import requests
import os
from uuid import uuid4

def download_image(image_url: str, save_dir: str = "downloads"):
    os.makedirs(save_dir, exist_ok=True)

    filename = f"{uuid4()}.jpg"
    filepath = os.path.join(save_dir, filename)

    response = requests.get(image_url)
    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath
    