# PinSense Project Technical Flow

## Overview
PinSense is a smart Pinterest board organizer that leverages computer vision and machine learning to automatically categorize and tag user pins. The system uses CLIP (Contrastive Language-Image Pretraining) for generating image embeddings, enabling clustering, aesthetic analysis, and personalized recommendations.

## Architecture
- **Backend**: Python-based FastAPI application
- **Frontend**: (Not implemented in current codebase)
- **ML Model**: CLIP via SentenceTransformers for image embeddings
- **Data Flow**: Images → Embeddings → Clustering/Analysis → Recommendations

## Step-by-Step Technical Flow

### 1. Project Setup
- Install Python dependencies from `backend/requirements.txt` (FastAPI, Uvicorn)
- Additional runtime dependencies: `sentence-transformers`, `Pillow` (PIL), `requests`
- Run the backend server using Uvicorn on the FastAPI app in `backend/app/main.py`

### 2. User Interaction (Conceptual - Frontend Not Implemented)
- User provides an image URL or uploads an image file
- Frontend (when implemented) would send this to the backend API

### 3. Image Submission
- **Endpoint**: `POST /api/submit-pin`
- **Input**: JSON with `image_url` field
- **Process**:
  - Receive image URL in request body
  - Call `download_image()` from `app/utils/image_downloader.py`
  - Download image from URL using `requests`
  - Save to `backend/downloads/` with UUID filename
  - Return success status and file path

### 4. Embedding Generation
- **Endpoint**: `POST /api/embed`
- **Input**: Image file upload
- **Process**:
  - Receive uploaded image file
  - Open image using PIL (Pillow) and convert to RGB
  - Load CLIP model (`clip-ViT-B-32`) via SentenceTransformers
  - Generate embedding vector using `model.encode(image)`
  - Return embedding as list of floats

### 5. Clustering and Analysis (Not Implemented)
- Use generated embeddings for:
  - K-means or hierarchical clustering to group similar images
  - Aesthetic tagging based on embedding analysis
  - Board suggestions and recommendations

### 6. Data Storage
- Downloaded images stored in `backend/downloads/`
- Models and utilities in respective directories
- No database integration visible in current codebase

## Key Components

### Backend Structure
- `app/main.py`: Main FastAPI application with CORS middleware and routes
- `app/routers/embedding_router.py`: API router for embedding endpoints
- `app/services/embedding_service.py`: Service layer for ML model interaction
- `app/utils/image_downloader.py`: Utility for downloading images from URLs

### Dependencies
- **FastAPI**: Web framework for API development
- **Uvicorn**: ASGI server for running FastAPI
- **SentenceTransformers**: For CLIP model and embedding generation
- **Pillow**: Image processing library
- **Requests**: HTTP library for downloading images

## Running the Project
1. Navigate to `backend/` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Install additional packages: `pip install sentence-transformers pillow requests`
4. Run server: `uvicorn app.main:app --reload`
5. API available at `http://localhost:8000`
6. Test endpoints with tools like Postman or curl

## Future Development
- Implement frontend for user interface
- Add clustering algorithms for pin grouping
- Integrate database for persistent storage
- Implement recommendation engine
- Add authentication and user management