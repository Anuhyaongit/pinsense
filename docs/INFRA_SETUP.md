# Infrastructure Setup Guide: Docker & Jenkins for PinSense

## Overview

**Docker** packages your application into containers (lightweight, isolated environments) so it runs the same everywhere.

**Jenkins** is a CI/CD (Continuous Integration/Continuous Deployment) automation server that automatically tests and deploys your code when you push changes.

### How They Work Together
```
You push code to GitHub
         ↓
Jenkins detects the change
         ↓
Jenkins pulls your code
         ↓
Jenkins builds Docker images
         ↓
Jenkins runs tests in containers
         ↓
Jenkins deploys to production (if tests pass)
```

---

## Phase 1: Docker Setup (LOCAL DEVELOPMENT)

### Step 1.1: Understand the Files We'll Create

```
backend/
├── Dockerfile           # Instructions to build backend container
├── .dockerignore        # Files to ignore when building

frontend/
├── Dockerfile           # Instructions to build frontend container
├── .dockerignore        # Files to ignore when building

docker-compose.yml      # Run both backend & frontend together locally
```

### Step 1.2: Create Backend Dockerfile

This tells Docker how to:
1. Start with a base Python image
2. Install dependencies
3. Copy your code
4. Run the server

**Location:** `backend/Dockerfile`

### Step 1.3: Create Frontend Dockerfile

Similar to backend, but for your Node.js frontend.

**Location:** `frontend/Dockerfile`

### Step 1.4: Create docker-compose.yml

Orchestrates running backend + frontend together with networking.

**Location:** `docker-compose.yml` (root)

### Step 1.5: Test Locally

```bash
docker-compose up
```

This builds and runs both containers. Your app will be accessible at `http://localhost:3000` (frontend) and `http://localhost:8000` (backend).

---

## Phase 2: Jenkins Setup (AUTOMATED DEPLOYMENT)

### Step 2.1: Jenkins Server Setup

Install Jenkins on a server (or use Docker for Jenkins too):
```bash
# Option A: Using Docker
docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

# Option B: Install on Ubuntu server
# We'll provide commands later
```

### Step 2.2: Create Jenkinsfile

A `Jenkinsfile` is a script that tells Jenkins what to do:
- Checkout code
- Run tests
- Build Docker images
- Push to registry
- Deploy

**Location:** `Jenkinsfile` (root)

### Step 2.3: Jenkins Configuration

In Jenkins UI (http://localhost:8080):
1. Create a new Pipeline job
2. Point it to your GitHub repo
3. Set it to read the `Jenkinsfile`
4. Add webhook to GitHub (auto-trigger on push)

---

## What You'll Need

- Docker installed on your machine
- Docker Hub account (for storing images)
- GitHub repo set up
- Jenkins server (local or cloud)
- Basic knowledge of Linux commands

---

## Next Steps

1. **Today:** Set up Docker locally (Phases 1.1-1.5)
2. **Tomorrow:** Test everything works locally
3. **Day 3:** Set up Jenkins server
4. **Day 4:** Create and test Jenkinsfile
5. **Day 5:** Deploy to production!

