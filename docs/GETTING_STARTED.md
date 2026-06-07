# Getting Started: First 24 Hours

## Day 1: Set Up Docker Locally ✅ (DO THIS FIRST)

### Morning (30 min)
- [ ] Install Docker Desktop: https://www.docker.com/products/docker-desktop
- [ ] Verify installation: `docker --version`
- [ ] Read [INFRA_SETUP.md](INFRA_SETUP.md) overview

### Afternoon (1 hour)
- [ ] Create `backend/requirements.txt`:
  ```
  flask==2.3.0
  gunicorn==21.0.0
  requests==2.31.0
  ```

- [ ] Create `frontend/package.json`:
  ```bash
  cd frontend && npm init -y
  npm install react react-dom
  npm install -D react-scripts
  ```

- [ ] Try building backend image:
  ```bash
  docker build -t pinsense-backend:test ./backend
  ```

### Evening (30 min)
- [ ] Test Docker Compose:
  ```bash
  docker-compose up
  ```
- [ ] Visit http://localhost:3000 (should see your frontend)
- [ ] Test backend: `curl http://localhost:8000`

---

## Day 2: Understand Your Current Setup

- [ ] What Python framework are you using? Flask? FastAPI?
  - Edit `backend/Dockerfile` CMD line if needed (see comments)
  
- [ ] What frontend framework? React? Vue? Next.js?
  - Update `frontend/Dockerfile` build command if needed

- [ ] Test docker-compose again with correct commands

---

## Day 3: Set Up Jenkins

- [ ] Start Jenkins container:
  ```bash
  docker run -d -p 8080:8080 -p 50000:50000 \
    -v jenkins_home:/var/jenkins_home \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --name jenkins \
    jenkins/jenkins:lts
  ```

- [ ] Access Jenkins at http://localhost:8080
  - Get password: `docker logs jenkins | grep -i password`

- [ ] Install suggested plugins

- [ ] Follow Step 2.4-2.5 in [DOCKER_JENKINS_GUIDE.md](DOCKER_JENKINS_GUIDE.md)

---

## Day 4: Test Jenkins Pipeline

- [ ] Create Docker Hub account (if not already)
- [ ] Add Docker Hub credentials to Jenkins
- [ ] Create Pipeline job pointing to your repo + Jenkinsfile
- [ ] Make a test commit to trigger pipeline
- [ ] View build logs in Jenkins

---

## Common Questions Beginners Ask

### Q: What's the difference between Docker and Docker Compose?
**A:** 
- **Docker**: Runs ONE container (your backend OR frontend)
- **Docker Compose**: Manages MULTIPLE containers together + networking

### Q: Why do we need Jenkins if Docker already works?
**A:**
- Docker = packaging your app
- Jenkins = automating the process of testing → building → deploying

### Q: How do I debug if something breaks?
```bash
# See what's running
docker ps

# Check logs
docker logs container_name

# Enter a container
docker exec -it container_name bash

# See network
docker network ls
```

### Q: What about environment variables?
```bash
# In docker-compose.yml:
environment:
  - DATABASE_URL=postgresql://user:pass@db:5432/pinsense

# In Dockerfile:
ENV FLASK_ENV=production
```

### Q: How do I deploy to a real server?
See "Production Deployment" section in [DOCKER_JENKINS_GUIDE.md](DOCKER_JENKINS_GUIDE.md)

---

## Files You Just Got

```
📦 pinsense/
├── 📄 INFRA_SETUP.md                  ← High-level overview
├── 📄 DOCKER_JENKINS_GUIDE.md         ← Detailed reference + troubleshooting
├── 📄 GETTING_STARTED.md              ← This file
├── 📄 Jenkinsfile                     ← Jenkins automation script
├── 📄 docker-compose.yml              ← Run locally: backend + frontend
├── 📁 backend/
│   ├── 📄 Dockerfile                  ← Build backend container
│   ├── 📄 .dockerignore               ← Exclude files from container
│   └── 📄 requirements.txt            ← Python dependencies
└── 📁 frontend/
    ├── 📄 Dockerfile                  ← Build frontend container
    ├── 📄 .dockerignore               ← Exclude files from container
    └── 📄 package.json                ← Node dependencies
```

---

## Next: Tell Me About Your Stack

Reply with:

1. **Backend**: What framework? (Flask, FastAPI, Django, etc.)
2. **Frontend**: What framework? (React, Vue, Next.js, etc.)
3. **Database**: Do you have one? (PostgreSQL, MongoDB, etc.)
4. **Where to deploy**: (AWS, Heroku, DigitalOcean, personal server, etc.)

This will help me optimize your setup! 🚀

