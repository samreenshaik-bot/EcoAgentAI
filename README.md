# EcoAgentAI

# 🌱 EcoAgent AI

**Intelligent Sustainability Advisor & Carbon Tracking Platform**

An AI-powered web application that helps users understand, track, and reduce their personal carbon footprint through real-time analytics, personalized recommendations, and comprehensive sustainability tracking.

![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Features

### 📊 **Analytics Dashboard**
- Real-time carbon footprint calculation
- KPI metrics with eco-score rating
- Interactive Plotly visualizations
- Monthly goal tracking and progress

### 🤖 **AI Sustainability Advisor**
- Google Gemini 3.5 powered recommendations
- RAG (Retrieval-Augmented Generation) knowledge base
- Personalized sustainability action plans
- Q&A interface for sustainability questions

### 📄 **Smart Bill Analyzer**
- Automated PDF bill extraction
- Electricity and water consumption detection
- Auto-population to dashboard
- Support for multiple utility formats

### 🎯 **Goals & Progress Tracking**
- Set monthly/annual carbon targets
- Create custom sustainability goals
- Visual progress gauges and charts
- Achievement badge system

### 💡 **Eco Tips & Advice**
- 10+ personalized sustainability tips
- Impact level indicators (High/Medium/Low)
- Random tip carousel
- Sustainability quick facts

### 📜 **PDF Report Generation**
- Comprehensive sustainability reports
- User impact analysis
- AI-generated recommendations
- Download and share functionality

---

## 🌍 UN Sustainable Development Goals

Aligned with **SDG 7, 12, and 13:**
- ⚡ **SDG 7**: Affordable & Clean Energy
- ♻️ **SDG 12**: Responsible Consumption & Production
- 🌍 **SDG 13**: Climate Action

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit 1.35.0 |
| **AI Models** | Google Gemini 3.5, Ollama |
| **RAG Framework** | LangChain 0.2.1 |
| **Vector DB** | ChromaDB 0.5.0 |
| **Analytics** | Plotly, Pandas, NumPy |
| **PDF Processing** | PyMuPDF, PyPDF, ReportLab |
| **ML** | PyTorch, Transformers |

---

## 📋 Requirements

- Python 3.11+
- pip or conda
- Google Gemini API key (free)
- 500MB disk space

---

## 🚀 Quick Start (Local Development)

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/ecoagent-ai.git
cd ecoagent-ai
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
```bash
cp .env.example .env
# Edit .env and add your Google API key
```

### 5. Run Application
```bash
streamlit run app.py
```

**App opens at:** http://localhost:8501

---

## 📚 Project Structure

```
ecoagent-ai/
├── app.py                          # Landing page
├── styles.py                        # Global CSS theming
├── requirements.txt                 # Dependencies
├── DEPLOYMENT_GUIDE.md             # Deployment instructions
├── ENHANCEMENT_GUIDE.md            # Feature guide
│
├── pages/
│   ├── dashboard.py               # Analytics dashboard
│   ├── sustainability_advisor.py   # AI advisor
│   ├── upload_bill.py             # Bill analyzer
│   ├── reports.py                 # Report generation
│   ├── goals.py                   # Goals & progress
│   └── eco_tips.py                # Sustainability tips
│
├── ai/
│   ├── ai_client.py               # LLM wrapper
│   ├── rag_pipeline.py            # RAG implementation
│   └── recommender.py             # Recommendation engine
│
├── utils/
│   ├── calculator.py              # Carbon footprint
│   ├── eco_score.py               # Scoring engine
│   ├── pdf_extractor.py           # PDF parsing
│   ├── report_gen.py              # PDF reports
│   └── goals_tracking.py          # Goals system
│
├── data/
│   └── chroma_db/                 # Vector database
│
├── knowledge_base/                # PDF documents
├── reports/                       # Generated PDFs
│
├── .streamlit/
│   └── config.toml                # Streamlit config
│
├── Dockerfile                     # Docker image
├── docker-compose.yml             # Docker compose
├── Procfile                       # Heroku deploy
└── runtime.txt                    # Python version
```

## 📖 Usage Guide

### **Dashboard**
1. Enter your monthly consumption data
2. Select transport mode (Car, Bus, Train, Bike)
3. Click "Recalculate Now"
4. View your carbon footprint and metrics

### **Goals & Progress**
1. Set monthly/annual targets
2. Create custom goals with deadlines
3. Track progress over time
4. Earn achievement badges

### **Eco Tips**
1. Get personalized tips based on your usage
2. View impact levels (High/Medium/Low)
3. Read sustainability quick facts


## 📊 Data & Privacy

- **Local Storage**: All user data stored locally in `data/`
- **No Cloud**: No automatic data sent to external servers
- **PDF Bills**: Processed locally, never uploaded
- **Optional API**: Google Gemini API for AI features only

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

# Verify API key is set
echo $GOOGLE_API_KEY
```

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👥 Authors

- **Development**: AI Sustainability Team
- **AI Models**: Google Gemini, LangChain
- **Framework**: Streamlit

---

## 🙏 Acknowledgments

- UN Sustainable Development Goals
- Google Gemini AI API
- Streamlit Community
- ChromaDB Vector Store
- LangChain Framework

---

**Made with ❤️ for a sustainable future 🌍**

Give us a ⭐ if you find this project helpful!


---

## 🌍 SDG Alignment
This project directly contributes to:
- **SDG 7 (Affordable and Clean Energy)**: Promoting energy efficiency via consumption analysis.
- **SDG 12 (Responsible Consumption and Production)**: Encouraging sustainable habits through data.
- **SDG 13 (Climate Action)**: Reducing individual carbon footprints through AI-driven insights.

#check out in application: https://ecoagentai.onrender.com/

