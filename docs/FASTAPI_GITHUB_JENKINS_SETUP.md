# FastAPI + PostgreSQL + GitHub Pages + Jenkins Setup Guide

## 🎯 Your Tech Stack

- **Backend**: FastAPI + PostgreSQL
- **Frontend**: React → GitHub Pages
- **Deployment**: Jenkins + Docker + GitHub Actions
- **Database**: PostgreSQL (in Docker)

---

## 📋 Quick Architecture Overview

```
                     GitHub Repository
                            ↓
            ┌────────────────┼────────────────┐
            ↓                ↓                ↓
      GitHub Actions   GitHub Actions    Jenkins
      (Frontend Tests) (Backend Tests)  (Full Deploy)
            ↓                ↓                ↓
      GitHub Pages    Codecov Report   Docker Registry
                                            ↓
                                    Production Server
```

---

## 🚀 Phase 1: Local Setup (TODAY)

### Step 1: Update Requirements
Your backend `requirements.txt` now includes:
- FastAPI (async web framework)
- Uvicorn (ASGI server)
- SQLAlchemy (database ORM)
- Psycopg2 (PostgreSQL driver)
- Pytest (testing)

### Step 2: Create React Frontend
```bash
cd frontend
npx create-react-app .
# OR for Vite:
npm create vite@latest . -- --template react
npm install
```

### Step 3: Update package.json for GitHub Pages
```bash
cd frontend
npm install --save-dev gh-pages
```

Then update `package.json`:
```json
{
  "name": "pinsense",
  "homepage": "https://your-username.github.io/pinsense",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "deploy": "gh-pages -d build"
  }
}
```

### Step 4: Test Local Docker Setup
```bash
# Start everything
docker-compose up

# In another terminal
curl http://localhost:8000/docs        # FastAPI docs
curl http://localhost:3000             # React app
```

### Step 5: Verify Database Connection
```bash
# Enter PostgreSQL container
docker exec -it pinsense_db psql -U pinsense_user -d pinsense_db

# View tables
\dt

# Exit
\q
```

---

## 🔧 Phase 2: GitHub Setup

### Step 2.1: Create GitHub Personal Access Token
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Click "Generate new token (classic)"
3. Scopes: `repo`, `workflow`
4. Copy the token (save it safely!)

### Step 2.2: Enable GitHub Pages
1. Go to your repo → Settings → Pages
2. Source: `Deploy from a branch`
3. Branch: `gh-pages` (will be created by GitHub Actions)
4. Click Save

### Step 2.3: Add GitHub Secrets
1. Go to Repo → Settings → Secrets and variables → Actions
2. Add these secrets:

| Secret Name | Value |
|------------|--------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password |
| `GITHUB_TOKEN` | Personal access token from Step 2.1 |

---

## 🔄 Phase 3: GitHub Actions Automation

### What GitHub Actions Does
- **On every push to main**: Runs tests, builds, and deploys
- **No Jenkins needed for frontend** (though you can use both!)
- **Automatic deployment to GitHub Pages**

### Workflows Included

#### 1. **deploy-frontend.yml**
- Runs on any change to `frontend/` folder
- Builds React app
- Deploys to GitHub Pages
- **Access at**: `https://your-username.github.io/pinsense`

#### 2. **test-backend.yml**
- Runs on any change to `backend/` folder
- Starts PostgreSQL in test environment
- Runs pytest with coverage
- Uploads coverage to Codecov

#### 3. **build-docker.yml**
- Runs on main branch push
- Builds Docker images
- Pushes to Docker Hub

### View Workflow Status
1. Go to repo → Actions tab
2. Click on workflow run
3. See detailed logs

---

## 🐳 Phase 4: Jenkins Setup (For Advanced Deployment)

Jenkins is optional now but useful for:
- Complex deployment logic
- Multiple environment deployments
- Scheduled deployments
- Manual approval gates

### Step 4.1: Start Jenkins with Docker
```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts
```

### Step 4.2: Initial Jenkins Setup
1. Get initial password:
   ```bash
   docker logs jenkins | grep -i "initial admin password"
   ```

2. Access http://localhost:8080
3. Install suggested plugins
4. Create admin user

### Step 4.3: Install Required Jenkins Plugins
1. Manage Jenkins → Manage Plugins
2. Available tab → Search and install:
   - Pipeline
   - Docker Pipeline
   - GitHub Integration
   - Email Extension

### Step 4.4: Add Jenkins Credentials
1. Manage Jenkins → Manage Credentials
2. System → Global credentials
3. Add Credentials:

**Docker Hub Credentials**
- Kind: Username with password
- Username: `your_docker_username`
- Password: `your_docker_password`
- ID: `docker-hub-credentials`

**GitHub Credentials**
- Kind: GitHub App or Personal access token
- Token: (your GitHub token)
- ID: `github-credentials`

### Step 4.5: Create Jenkins Pipeline Job
1. Dashboard → New Item
2. Name: "PinSense"
3. Type: Pipeline
4. OK
5. In Pipeline section:
   - Definition: Pipeline script from SCM
   - SCM: Git
   - Repository: `https://github.com/your-username/pinsense.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`
6. Save

### Step 4.6: Add GitHub Webhook to Jenkins
1. Go to repo Settings → Webhooks → Add webhook
2. Payload URL: `http://your-jenkins-server:8080/github-webhook/`
3. Content type: `application/json`
4. Events: Push events
5. Active: ✓
6. Add webhook

---

## 📊 Deployment Workflow (Automated)

### What Happens When You Push Code:

```bash
git add .
git commit -m "Add new feature"
git push origin main
```

**Automatically triggers:**

1. **GitHub Actions** (Frontend):
   - ✓ Tests React components
   - ✓ Builds optimized bundle
   - ✓ Deploys to GitHub Pages (~2 min)
   - Access at: https://your-username.github.io/pinsense

2. **GitHub Actions** (Backend):
   - ✓ Starts PostgreSQL container
   - ✓ Runs pytest
   - ✓ Uploads coverage report
   - ✓ Builds Docker image
   - ✓ Pushes to Docker Hub

3. **Jenkins** (Optional, for server deployment):
   - ✓ Pulls from Docker Hub
   - ✓ Runs on production server
   - ✓ Performs smoke tests
   - ✓ Sends notifications

---

## 🌐 GitHub Pages Configuration

### Make Frontend Work with GitHub Pages

Update your React app to work with GitHub Pages subdirectory:

**In `frontend/src/index.js`:**
```jsx
import { BrowserRouter as Router } from 'react-router-dom';

<Router basename="/pinsense">
  <App />
</Router>
```

**Or in `frontend/.env`:**
```
PUBLIC_URL=/pinsense
```

### Local Testing of GitHub Pages Build
```bash
cd frontend
npm run build
npx serve -s build -l 3000
```

Then visit `http://localhost:3000/pinsense`

---

## 🗄️ Database Management

### Connect to PostgreSQL

**Locally in Docker:**
```bash
docker exec -it pinsense_db psql -U pinsense_user -d pinsense_db
```

**From Python (in backend):**
```python
from sqlalchemy import create_engine

engine = create_engine(os.getenv('DATABASE_URL'))
```

### Run Database Migrations
```bash
# In backend container
docker-compose exec backend alembic upgrade head

# Or locally
alembic upgrade head
```

### Backup Database
```bash
docker exec pinsense_db pg_dump -U pinsense_user pinsense_db > backup.sql
```

### Restore Database
```bash
docker exec -i pinsense_db psql -U pinsense_user pinsense_db < backup.sql
```

---

## 🔑 Environment Variables

### Local (`.env` file)
```env
ENV=development
DEBUG=True
DATABASE_URL=postgresql://pinsense_user:pinsense_secure_pass_change_me@db:5432/pinsense_db
REACT_APP_API_URL=http://localhost:8000
```

### Production (Set in deployment)
```env
ENV=production
DEBUG=False
DATABASE_URL=postgresql://user:secure_password@production-db:5432/pinsense_db
REACT_APP_API_URL=https://api.your-domain.com
SECRET_KEY=your_secure_key
```

---

## ✅ Production Deployment Checklist

- [ ] Create `.env` file (never commit it!)
- [ ] Add `.env` to `.gitignore`
- [ ] Update Docker Hub credentials in GitHub Secrets
- [ ] Verify GitHub Pages is enabled
- [ ] Test workflows on a test branch first
- [ ] Set up production server with Docker
- [ ] Configure domain DNS
- [ ] Set up SSL certificate (Let's Encrypt)
- [ ] Test full deployment pipeline
- [ ] Monitor logs in production

---

## 🐛 Troubleshooting

### GitHub Actions Workflow Fails
```bash
# Check workflow logs
GitHub → Actions → Click failed workflow → Click job

# Common fixes:
- Check environment variables in secrets
- Verify Docker Hub credentials
- Check Node/Python versions match
```

### Frontend not deploying to GitHub Pages
```bash
# Check GitHub Pages settings
Settings → Pages → Ensure source is "Deploy from a branch"

# Verify package.json has homepage field
"homepage": "https://your-username.github.io/pinsense"
```

### Backend not connecting to database
```bash
# Check database is running
docker ps | grep postgres

# Check DATABASE_URL is correct
echo $DATABASE_URL

# Test connection
docker-compose exec backend python -c "from sqlalchemy import create_engine; engine = create_engine(os.getenv('DATABASE_URL')); print(engine.execute('SELECT 1'))"
```

---

## 📚 File Structure

```
pinsense/
├── .github/workflows/
│   ├── deploy-frontend.yml          # → GitHub Pages
│   ├── test-backend.yml             # → Codecov
│   └── build-docker.yml             # → Docker Hub
├── Jenkinsfile                      # Jenkins automation
├── docker-compose.yml               # Local dev environment
├── .env.example                     # Example env variables
├── backend/
│   ├── Dockerfile                   # FastAPI container
│   ├── requirements.txt             # Python dependencies
│   ├── init.sql                     # Database schema
│   └── app/main.py                  # FastAPI app
└── frontend/
    ├── Dockerfile                   # React container
    ├── package.json                 # Node dependencies
    └── src/App.jsx                  # React app
```

---

## 🎓 Learning Path

**Day 1-2**: Get Docker working locally ✓
**Day 3**: Enable GitHub Pages + GitHub Actions
**Day 4**: Test frontend deployment
**Day 5**: Configure backend tests
**Day 6**: Set up Jenkins (optional)
**Day 7**: Deploy to production!

---

## 🆘 Need Help?

1. Check GitHub Actions logs: Repo → Actions → Click run
2. Check Jenkins logs: Jenkins UI → Click build → Console output
3. Check Docker logs: `docker logs container_name`
4. Check database: `docker exec pinsense_db psql -U pinsense_user -d pinsense_db`

