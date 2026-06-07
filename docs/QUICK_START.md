# Quick Start: FastAPI + PostgreSQL + GitHub Pages + Jenkins

## 🏃 Start Here (Next 30 Minutes)

### 1. Verify Your Backend Framework
```bash
cd backend
head -5 app/main.py
```
Should show:
```python
from fastapi import FastAPI
```
✅ Great! You're using FastAPI

### 2. Update Frontend (Pick One)

**Option A: React (Recommended)**
```bash
cd frontend
npx create-react-app .
# or Vite: npm create vite@latest . -- --template react
npm install
```

**Option B: Already have React setup**
Just ensure `package.json` exists:
```bash
cd frontend
npm install
```

### 3. Test Locally (5 minutes)
```bash
# From repo root
docker-compose up

# In another terminal
curl http://localhost:8000/docs
curl http://localhost:3000
```

✅ Should see FastAPI docs and React app!

---

## 📱 GitHub Pages Setup (10 minutes)

### Step 1: Update package.json
In `frontend/package.json`, add:
```json
{
  "homepage": "https://YOUR_GITHUB_USERNAME.github.io/pinsense",
  "scripts": {
    "deploy": "gh-pages -d build"
  }
}
```

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username!

### Step 2: Install gh-pages
```bash
cd frontend
npm install --save-dev gh-pages
```

### Step 3: Enable in GitHub
1. Go to your repo on GitHub
2. Settings → Pages
3. Source: "Deploy from a branch"
4. Branch: `gh-pages`
5. Save

---

## 🤖 GitHub Actions Setup (10 minutes)

### Step 1: Add GitHub Secrets
1. Go to repo → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add these:

```
DOCKER_USERNAME = your_docker_hub_username
DOCKER_PASSWORD = your_docker_hub_password
```

### Step 2: Done! ✅
Workflows are already created in `.github/workflows/`:
- Frontend auto-deploys to GitHub Pages on push
- Backend tests run automatically
- Docker images build automatically

---

## 🚀 First Deployment (5 minutes)

### Make a Small Change
```bash
# Edit a file
echo "# Updated" >> README.md

# Commit and push
git add .
git commit -m "Test CI/CD"
git push origin main
```

### Watch It Deploy!
1. Go to GitHub repo → Actions
2. See your workflow running
3. Check the logs
4. Visit your frontend at: `https://YOUR_GITHUB_USERNAME.github.io/pinsense`

---

## 🔄 Daily Workflow

```bash
# Make changes
nano backend/app/main.py

# Test locally
docker-compose up

# Commit
git add .
git commit -m "Add new endpoint"
git push origin main

# GitHub Actions automatically:
# ✓ Tests code
# ✓ Builds containers
# ✓ Deploys frontend to GitHub Pages
# ✓ Pushes backend to Docker Hub
```

---

## 🐳 Jenkins Setup (Optional - for advanced deployment)

Only do this if you have a production server to deploy to.

```bash
# Start Jenkins
docker run -d -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts

# Get password
docker logs jenkins | grep -i "initial admin password"

# Visit http://localhost:8080
```

---

## ✅ Verify Everything Works

```bash
# 1. Backend running?
curl http://localhost:8000/docs
# Should see FastAPI interactive docs ✓

# 2. Frontend running?
curl http://localhost:3000
# Should return HTML ✓

# 3. Database running?
docker exec pinsense_db psql -U pinsense_user -d pinsense_db -c "SELECT 1"
# Should return 1 ✓

# 4. All containers healthy?
docker ps
# Should see 3 containers: backend, frontend, db ✓
```

---

## 📝 Next Steps

1. **Today**: Follow "Start Here" section above
2. **Tomorrow**: Make your first commit and watch GitHub Actions deploy
3. **This Week**: Add API endpoints to backend
4. **Next Week**: Deploy to production server with Jenkins

---

## 💡 Tips

- **Check GitHub Actions logs** when something breaks
- **Never commit `.env` file** (add to `.gitignore`)
- **Database changes**? Update `backend/init.sql`
- **Need to restart everything?** `docker-compose down && docker-compose up`

---

## 🆘 Common Issues

### "GitHub Pages not showing my app"
1. Check Settings → Pages → Source is set correctly
2. Check `package.json` has `"homepage"` field
3. Check GitHub Actions `deploy-frontend.yml` succeeded

### "Backend tests failing"
1. Check PostgreSQL is running: `docker ps`
2. Check database URL in test workflow
3. Look at GitHub Actions logs for detailed error

### "Docker image won't build"
1. Check `requirements.txt` (backend) exists and is valid
2. Check `package.json` (frontend) exists
3. Run `docker build` manually to see full error:
   ```bash
   docker build -t test ./backend
   ```

