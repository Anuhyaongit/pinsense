from fastapi import FastAPI

app = FastAPI(
    title="PinSense Backend",
    description="Backend API for visual embeddings, clustering, and recommendations",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "PinSense backend is running!"}
