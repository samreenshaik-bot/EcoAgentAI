# ⚡ Quick Deployment Start Guide

**Choose your preferred deployment method and get your app live in minutes!**

---

## 🚀 30-Second Deployment (Streamlit Cloud - RECOMMENDED)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "EcoAgent AI v1.0"
git remote add origin https://github.com/YOUR_USERNAME/ecoagent-ai.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Click "Create app"
3. Select your GitHub repository
4. Choose branch: `main`
5. Set main file path: `app.py`
6. Click "Deploy"

**That's it! Your app is live! 🎉**

Your app will be available at: `https://ecoagent-ai-YOUR_USERNAME.streamlit.app`

---

## 🐳 Docker Deployment (Any Platform)

### Test Locally First
```bash
# Build image
docker build -t ecoagent-ai .

# Run container
docker run -p 8501:8501 ecoagent-ai

# Visit http://localhost:8501
```

### Deploy to DigitalOcean
```bash
# 1. Create account at digitalocean.com
# 2. Create new App
# 3. Connect your GitHub repo
# 4. Deploy (auto-detects Dockerfile)
```

---

## 🚂 Heroku Deployment

```bash
# Install Heroku CLI
npm install -g heroku

# Login to Heroku
heroku login

# Create app
heroku create ecoagent-ai

# Push code
git push heroku main

# View logs
heroku logs --tail
```

App URL: `https://ecoagent-ai.herokuapp.com`

---

## 🌐 Complete Deployment Guide

**See detailed instructions for:**
- Streamlit Cloud (5 min) ⭐
- Heroku (10 min)
- Docker + DigitalOcean (20 min)
- AWS (30 min)
- Google Cloud Run (30 min)
- Self-hosted with Nginx (45 min)

👉 [Full DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

---

## 🔐 Before Deploying

### 1. Create `.env` file with your API key
```bash
cp .env.example .env
# Add your Google Gemini API key to .env
```

### 2. Test locally
```bash
streamlit run app.py
# Visit http://localhost:8501 and verify everything works
```

### 3. Update GitHub secrets (for CI/CD)
```bash
# Add to GitHub repo Settings > Secrets:
GOOGLE_API_KEY=your-key-here
```

---

## ✅ Post-Deployment Checklist

- [ ] App loads without errors
- [ ] Dashboard displays correctly
- [ ] Can generate recommendations
- [ ] PDF uploads work
- [ ] Reports generate successfully
- [ ] All pages load without console errors

---

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| API key error | Add GOOGLE_API_KEY to environment variables |
| Slow loading | Clear browser cache, restart app |
| Port already in use | Kill process on port 8501: `lsof -ti:8501 \| xargs kill -9` |

---

## 📊 Monitoring Your Deployment

### Streamlit Cloud
- Dashboard: https://share.streamlit.io
- Logs: Viewable in app settings
- Analytics: Built-in

### Heroku
```bash
heroku logs --tail
heroku status
```

### Docker/DigitalOcean
- Logs: `docker logs <container-id>`
- Metrics: DigitalOcean dashboard

---

## 🎯 Next Steps

1. **Streamlit Cloud** (Recommended for beginners)
2. Get your custom domain (optional)
3. Share your app with friends
4. Collect feedback
5. Deploy improvements
6. Scale to other platforms as needed

---

**Questions? Check [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed walkthroughs!**
