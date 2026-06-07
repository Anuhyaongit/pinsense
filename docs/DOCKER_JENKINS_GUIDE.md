# Docker & Jenkins Quick Reference

## Prerequisites Checklist
- [ ] Docker installed (`docker --version`)
- [ ] Docker Hub account (or private registry)
- [ ] Git repository on GitHub
- [ ] Jenkins server running
- [ ] requirements.txt in backend
- [ ] package.json in frontend

---

## 🐳 PHASE 1: LOCAL DOCKER SETUP

### Step 1: Install Docker
```bash
# macOS
brew install docker

# Or download Docker Desktop:
# https://www.docker.com/products/docker-desktop
```

### Step 2: Create requirements.txt (Backend)
```bash
cd backend
# Add your Python dependencies:
echo "flask==2.3.0" >> requirements.txt
echo "gunicorn==21.0.0" >> requirements.txt
echo "requests==2.31.0" >> requirements.txt
# Add more as needed
```

### Step 3: Create package.json (Frontend)
If it doesn't exist:
```bash
cd frontend
npm init -y
npm install react react-dom
npm install -D react-scripts
```

### Step 4: Test Local Docker Build
```bash
# Build backend
docker build -t pinsense-backend:dev ./backend

# Build frontend
docker build -t pinsense-frontend:dev ./frontend

# List images
docker images
```

### Step 5: Run with Docker Compose
```bash
# Start all services
docker-compose up

# In another terminal, test the services
curl http://localhost:8000/health        # Backend
curl http://localhost:3000               # Frontend

# Stop services
docker-compose down
```

### Step 6: Useful Docker Commands
```bash
# View running containers
docker ps

# View logs from a container
docker logs container_id

# Stop all containers
docker stop $(docker ps -q)

# Remove unused images/volumes
docker system prune
```

---

## 🔧 PHASE 2: JENKINS SETUP

### Step 2.1: Start Jenkins with Docker
```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts
```

### Step 2.2: Access Jenkins
1. Open http://localhost:8080
2. Get initial password:
   ```bash
   docker logs jenkins | grep -i "password" | tail -1
   ```
3. Unlock Jenkins with the password

### Step 2.3: Install Plugins
1. Click "Install suggested plugins"
2. Wait for installation
3. Create first admin user

### Step 2.4: Add Docker Hub Credentials
1. Dashboard → Manage Jenkins → Manage Credentials
2. Click "System" → "Global credentials"
3. Click "Add Credentials"
4. Choose "Username and password"
5. Enter Docker Hub username/password
6. Set ID to `docker-hub-credentials`

### Step 2.5: Create Pipeline Job
1. Dashboard → New Item
2. Name: "PinSense Pipeline"
3. Choose: Pipeline
4. Click OK
5. Scroll to Pipeline section
6. Change "Definition" to "Pipeline script from SCM"
7. SCM: Git
8. Repository URL: `https://github.com/yourusername/pinsense.git`
9. Branch: `*/main`
10. Script Path: `Jenkinsfile`
11. Save

### Step 2.6: Add GitHub Webhook (Auto-trigger)
1. Go to your GitHub repo
2. Settings → Webhooks → Add webhook
3. Payload URL: `http://your-jenkins-server:8080/github-webhook/`
4. Content type: application/json
5. Events: Push events
6. Active: ✓
7. Add webhook

### Step 2.7: Test Pipeline
1. Make a small commit/push to main
2. Jenkins should automatically trigger the build
3. Click build to view logs

---

## 🚀 PRODUCTION DEPLOYMENT

### Prerequisites on Production Server
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Deploy Manually
```bash
# SSH into production server
ssh deploy@your-server

# Navigate to app directory
cd /app/pinsense

# Pull latest images
docker-compose pull

# Start services (recreates containers if images changed)
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 🐛 TROUBLESHOOTING

### Docker image won't build
```bash
# Check Docker is running
docker ps

# Check file permissions
chmod +x backend/Dockerfile

# Try without cache
docker build --no-cache -t myimage .
```

### Docker Compose connection error
```bash
# Ensure backend is fully started before frontend tries to connect
# Check docker-compose.yml has "depends_on"

# Manually test backend
docker exec pinsense_backend curl http://localhost:8000
```

### Jenkins not finding Jenkinsfile
```bash
# Ensure Jenkinsfile is in repo root
ls -la Jenkinsfile

# Check Pipeline → Script Path is correct
```

### Permission denied when deploying
```bash
# SSH key permission
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh

# Ensure deploy user is in docker group
sudo usermod -aG docker deploy
```

---

## 📚 LEARNING RESOURCES

- Docker: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- Jenkins: https://www.jenkins.io/doc/
- CI/CD Basics: https://www.atlassian.com/ci-cd

---

## ⚠️ SECURITY NOTES

- Never commit `.env` files with secrets
- Use Jenkins credentials for API keys/passwords
- Don't run Docker as root in production
- Use private Docker registry for sensitive images
- Set resource limits on containers
- Use HTTPS for Jenkins

