# 🚀 EcoAgent AI - Deployment Guide

## Overview
This guide covers multiple ways to deploy your EcoAgent AI Streamlit application to the web.

---

## **Option 1: Streamlit Cloud (EASIEST - Recommended) ⭐**

### Why Streamlit Cloud?
- ✅ Free tier with generous limits
- ✅ 1-click deployment from GitHub
- ✅ Automatic SSL/HTTPS
- ✅ Custom domain support
- ✅ No DevOps required

### Step 1: Prepare Your Repository
```bash
# Push your code to GitHub
git init
git add .
git commit -m "EcoAgent AI - Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ecoagent-ai.git
git push -u origin main
```

**Important Files to Include:**
```
ecoagent-ai/
├── requirements.txt          # ✅ Already exists
├── app.py
├── .streamlit/
│   └── config.toml          # NEW: Add this
├── pages/
│   ├── dashboard.py
│   ├── goals.py
│   ├── eco_tips.py
│   ├── sustainability_advisor.py
│   ├── upload_bill.py
│   └── reports.py
├── ai/
├── utils/
├── data/                     # Can be empty (git-ignored)
├── knowledge_base/          # Add sample PDFs
├── styles.py
└── .gitignore               # NEW: Add this
```

### Step 2: Create `.streamlit/config.toml`
```toml
[theme]
primaryColor = "#2e7d32"
backgroundColor = "#fafafa"
secondaryBackgroundColor = "#f5f5f5"
textColor = "#212121"
font = "sans serif"

[client]
showErrorDetails = false
maxUploadSize = 200  # MB

[logger]
level = "warning"

[server]
port = 8501
headless = true
runOnSave = true
```

### Step 3: Create `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
*.egg-info/

# Streamlit
.streamlit/secrets.toml
.streamlit/*.json

# Data & Cache
data/
.cache/
*.pkl
.chromadb/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

### Step 4: Update `requirements.txt` (Important!)
Make sure all dependencies are pinned to specific versions:

```txt
# Core UI & Analytics
streamlit==1.35.0
streamlit-option-menu==0.3.12
plotly==5.22.0
pandas==2.2.2
matplotlib==3.8.4

# AI & LLM
google-generativeai==0.5.2
langchain==0.2.1
langchain-google-genai==1.0.5
langchain-community==0.2.1
langchain-chroma==0.1.1
langchain-text-splitters==0.2.0
langchain-huggingface==0.0.1
sentence-transformers==3.0.0

# Vector Store & PDF
chromadb==0.5.0
pymupdf==1.24.4
pypdf==4.2.0
reportlab==4.2.0

# ML & NLP
torch==2.2.0
transformers==4.38.0
numpy==1.24.3
scikit-learn==1.4.0
```

### Step 5: Deploy on Streamlit Cloud

1. Go to **https://share.streamlit.io**
2. Click **"New app"**
3. Sign in with GitHub
4. Select repository: `your-username/ecoagent-ai`
5. Select branch: `main`
6. Select file: `app.py`
7. Click **Deploy!**

**Your app will be live in 2-3 minutes at:**
```
https://ecoagent-ai-yourname.streamlit.app
```

### Step 6: Handle Secrets (if needed)
If you use API keys, add them to Streamlit Cloud:
1. Go to app settings (gear icon)
2. Click **Secrets**
3. Add your secrets in TOML format:

```toml
[google]
api_key = "your-google-api-key-here"
```

Then access in code:
```python
import streamlit as st
api_key = st.secrets["google"]["api_key"]
```

---

## **Option 2: Heroku (Free-ish, More Control)**

### Prerequisites
- Heroku account (free tier has limitations)
- Heroku CLI installed

### Step 1: Create Heroku app
```bash
heroku login
heroku create ecoagent-ai-app
```

### Step 2: Create `Procfile` (in root directory)
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Step 3: Create `runtime.txt` (specify Python version)
```
python-3.11.8
```

### Step 4: Deploy
```bash
git push heroku main
```

### Step 5: View logs
```bash
heroku logs --tail
```

**Your app will be at:**
```
https://ecoagent-ai-app.herokuapp.com
```

---

## **Option 3: Docker + DigitalOcean App Platform**

### Step 1: Create `Dockerfile`
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--logger.level=warning"]
```

### Step 2: Build & test locally
```bash
docker build -t ecoagent-ai .
docker run -p 8501:8501 ecoagent-ai
```

### Step 3: Push to Docker Hub
```bash
docker tag ecoagent-ai YOUR_USERNAME/ecoagent-ai
docker push YOUR_USERNAME/ecoagent-ai
```

### Step 4: Deploy on DigitalOcean
1. Go to **DigitalOcean App Platform**
2. Connect GitHub repo
3. Select `Dockerfile` in root
4. Set port to 8501
5. Deploy

---

## **Option 4: AWS (Most Flexible)**

### Using AWS Elastic Beanstalk

### Step 1: Install EB CLI
```bash
pip install awsebcli
```

### Step 2: Initialize EB app
```bash
eb init -p python-3.11 ecoagent-ai --region us-east-1
```

### Step 3: Create `.ebextensions/streamlit.config`
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
  aws:elasticbeanstalk:cloudwatch:logs:
    StreamLogs: true
    DeleteOnTerminate: false

commands:
  01_install:
    command: pip install --no-cache-dir -r requirements.txt
```

### Step 4: Deploy
```bash
eb create ecoagent-prod
eb open
```

---

## **Option 5: Google Cloud Run (Recommended for scalability)**

### Step 1: Create `cloudbuild.yaml`
```yaml
steps:
  # Build the Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/ecoagent-ai', '.']
  
  # Push the image to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/ecoagent-ai']
  
  # Deploy to Cloud Run
  - name: 'gcr.io/cloud-builders/gke-deploy'
    args:
      - run
      - --filename=k8s/
      - --image=gcr.io/$PROJECT_ID/ecoagent-ai
      - --location=us-central1
```

### Step 2: Deploy
```bash
gcloud builds submit --config cloudbuild.yaml
gcloud run deploy ecoagent-ai \
  --image gcr.io/PROJECT_ID/ecoagent-ai \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## **Option 6: Self-Hosted with Nginx Reverse Proxy**

### Step 1: SSH into your server
```bash
ssh user@your-server.com
```

### Step 2: Install dependencies
```bash
sudo apt update
sudo apt install python3.11 python3-pip nginx supervisor
```

### Step 3: Clone repo and setup
```bash
cd /home/user
git clone https://github.com/YOUR_USERNAME/ecoagent-ai.git
cd ecoagent-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Create Supervisor config (`/etc/supervisor/conf.d/ecoagent.conf`)
```ini
[program:ecoagent]
directory=/home/user/ecoagent-ai
command=/home/user/ecoagent-ai/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true
autostart=true
autorestart=true
stderr_logfile=/var/log/ecoagent.err.log
stdout_logfile=/var/log/ecoagent.out.log
```

### Step 5: Configure Nginx
```nginx
server {
    listen 80;
    server_name ecoagent.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Step 6: Enable SSL with Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d ecoagent.com
```

---

## **Deployment Comparison**

| Option | Cost | Setup Time | Scalability | Best For |
|--------|------|-----------|-------------|----------|
| **Streamlit Cloud** | Free (generous) | 5 min | Good | Quick demos, personal projects |
| **Heroku** | $7-50/month | 10 min | Moderate | Small to medium apps |
| **DigitalOcean** | $5-40/month | 20 min | Good | Full control, affordable |
| **AWS** | Pay-as-you-go | 30 min | Excellent | Enterprise, high traffic |
| **Google Cloud Run** | Pay-as-you-go | 30 min | Excellent | Serverless, auto-scaling |
| **Self-hosted** | $5-50/month | 45 min | Limited | Maximum control, cost savings |

---

## **Post-Deployment Checklist**

### Security
- [ ] Hide API keys in environment variables/secrets
- [ ] Enable HTTPS/SSL
- [ ] Set up authentication if needed
- [ ] Rate limiting configured
- [ ] CORS headers configured

### Performance
- [ ] CDN enabled (if applicable)
- [ ] Database optimized
- [ ] Caching configured
- [ ] Monitoring set up

### Maintenance
- [ ] Error logging configured
- [ ] Uptime monitoring enabled
- [ ] Backup strategy in place
- [ ] CI/CD pipeline set up

---

## **Recommended Quick Start**

For fastest deployment (5 minutes):

```bash
# 1. Create GitHub repo and push code
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ecoagent-ai.git
git push -u origin main

# 2. Go to https://share.streamlit.io
# 3. Click "New app"
# 4. Select your repo and app.py
# 5. Click Deploy!

# Your app is now live! 🎉
```

---

## **Environment Variables for Production**

Create a `.env` file (don't commit to git):

```env
# Google Gemini API
GOOGLE_API_KEY=your-key-here

# Optional: Configure Streamlit
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_RUN_ON_SAVE=false
STREAMLIT_LOGGER_LEVEL=warning

# Optional: Database
DATABASE_URL=your-database-url
```

Then load in Python:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

---

## **Troubleshooting**

### App crashes on startup
```
Check logs: heroku logs --tail
Check requirements.txt for missing packages
Verify Python version compatibility
```

### Out of memory errors
```
Reduce file upload size in config
Optimize large computations
Use caching: @st.cache_data
```

### Slow performance
```
Enable Streamlit caching
Optimize database queries
Use async operations where possible
```

---

## **Next Steps**

1. **Choose deployment option** based on your needs
2. **Set up automatic deployments** (GitHub → Deploy)
3. **Configure monitoring** (uptime, errors, performance)
4. **Add custom domain** (optional)
5. **Set up SSL certificate** (HTTPS)
6. **Monitor usage** and scale as needed

Good luck deploying! 🚀
