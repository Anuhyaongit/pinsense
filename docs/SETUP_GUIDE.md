# PinSense Project: Complete Step-by-Step Guide

## **Part 1: Understanding the Project**

### What is PinSense?
PinSense is a **smart Pinterest board organizer** that uses AI to automatically analyze and organize pins. It:
- Extracts visual information from images using CLIP (machine learning model)
- Groups similar pins together
- Tags pins with aesthetic properties
- Suggests board organizations
- Recommends new pins based on your visual taste

### How It Works (The Flow)
1. **You save an image URL** → Extension captures it from Pinterest
2. **Backend downloads the image** → Stores it locally
3. **ML model analyzes the image** → Generates an "embedding" (mathematical representation)
4. **Embeddings enable analysis** → Compare images, find similarities, tag aesthetics
5. **Results come back** → Organized pins and recommendations

---

## **Part 2: Architecture Overview**

```
Your Computer
├── Browser (Chrome/Firefox)
│   └── PinSense Extension
│       └── Right-click "Add to PinSense"
│
├── Backend Server (Python/FastAPI)
│   ├── /api/submit-pin → Downloads images
│   ├── /api/embed → Generates embeddings
│   └── ML Model (CLIP) → Analyzes images
│
└── File Storage
    └── /backend/downloads/ → Saved images
```

---

## **Part 3: Prerequisites**

Before you start, you need:
- Python 3.8+ installed (`python --version`)
- pip (Python package manager - usually comes with Python)
- Git (optional, for version control)
- Chrome or Firefox browser (for the extension)

---

## **Part 4: Setup Instructions**

### **Step 1: Navigate to the project**
```bash
cd /Users/anuhya/Documents/pinsense
```

### **Step 2: Install Python dependencies**
```bash
cd backend
pip install -r requirements.txt
```

This installs:
- **FastAPI** — Web framework to create the API
- **Uvicorn** — Server to run the API

### **Step 3: Install additional dependencies**
```bash
pip install sentence-transformers pillow requests
```

This installs:
- **sentence-transformers** — Access to the CLIP model (for embeddings)
- **pillow** — Image processing library
- **requests** — Downloads images from URLs

### **Step 4: Verify installation**
```bash
python -c "import fastapi; import uvicorn; import sentence_transformers; print('✓ All dependencies installed!')"
```

---

## **Part 5: Running the Project**

### **Start the Backend Server**
```bash
cd /Users/anuhya/Documents/pinsense/backend
uvicorn app.main:app --reload
```

You'll see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

✅ **Backend is now running!** The API is available at `http://localhost:8000`

---

## **Part 6: Testing the API (Optional)**

### **Test 1: Check if server is alive**
```bash
curl http://localhost:8000
```
Expected response:
```json
{"message": "Backend is running!"}
```

### **Test 2: Submit an image URL**
```bash
curl -X POST http://localhost:8000/api/submit-pin \
  -H "Content-Type: application/json" \
  -d '{"image_url": "https://example.com/image.jpg"}'
```

### **Test 3: Generate embedding from an image**
Use Postman or curl to upload an image:
```bash
curl -X POST http://localhost:8000/api/embed \
  -F "file=@/path/to/image.jpg"
```

---

## **Part 7: Installing the Browser Extension**

### **For Chrome:**
1. Open Chrome → Go to `chrome://extensions/`
2. Enable **"Developer mode"** (toggle in top-right)
3. Click **"Load unpacked"**
4. Select `/Users/anuhya/Documents/pinsense/extension/` folder
5. You'll see the PinSense extension in your toolbar ✅

### **For Firefox:**
1. Open Firefox → Go to `about:debugging`
2. Click **"This Firefox"** in left sidebar
3. Click **"Load Temporary Add-on"**
4. Select `manifest.json` from the `extension/` folder

---

## **Part 8: Using the Extension**

1. **Make sure backend is running** (from Part 5)
2. **Go to Pinterest.com**
3. **Right-click any image** → Select **"Add to PinSense"**
4. You'll see a notification: **"Pin added successfully!"**
5. The image is downloaded to `/backend/downloads/`

---

## **Part 9: Project Structure Explained**

```
pinsense/
├── backend/                          # Python backend server
│   ├── app/
│   │   ├── main.py                  # FastAPI app & routes
│   │   ├── routers/
│   │   │   └── embedding_router.py  # /api/embed endpoint
│   │   ├── services/
│   │   │   └── embedding_service.py # CLIP model loading & inference
│   │   └── utils/
│   │       └── image_downloader.py  # Download images from URLs
│   ├── downloads/                    # Saved images go here
│   ├── requirements.txt              # Python dependencies
│   └── app.py                        # Entry point
│
├── extension/                        # Browser extension
│   ├── manifest.json                # Extension configuration
│   ├── background.js                # Context menu handler
│   ├── popup.html                   # Extension popup UI
│   └── popup.js                     # Settings storage
│
├── project_flow.md                  # Detailed technical flow
├── README.md                        # Project overview
└── .gitignore                       # Files to ignore in git
```

---

## **Part 10: Common Commands (Quick Reference)**

```bash
# Navigate to backend
cd /Users/anuhya/Documents/pinsense/backend

# Start server
uvicorn app.main:app --reload

# Install dependencies
pip install -r requirements.txt

# Check downloaded images
ls downloads/

# Stop server
# Press CTRL+C
```

---

## **Part 11: What's Next (Not Yet Implemented)**

- ❌ Database storage (currently just saves images)
- ❌ Frontend UI (not implemented)
- ❌ Clustering algorithm (group similar pins)
- ❌ Aesthetic tagging
- ❌ Recommendation engine
- ❌ User authentication

---

## **Troubleshooting**

| Problem | Solution |
|---------|----------|
| "Port 8000 already in use" | Change port: `uvicorn app.main:app --port 8001` |
| Extension can't connect to backend | Make sure backend is running; check URL in extension settings |
| "Module not found" errors | Run: `pip install -r requirements.txt` |
| Extension not appearing in Chrome | Check `chrome://extensions/` and ensure developer mode is ON |

---

**Now you have a complete understanding of PinSense!** 🎉
