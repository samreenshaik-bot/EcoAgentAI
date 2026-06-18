import streamlit as st
from styles import inject_custom_css

# Page Config
st.set_page_config(
    page_title="EcoAgent AI | Home",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS theme
inject_custom_css()

def main():
    # Hero Section
    st.markdown("""
        <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); 
                    padding: 50px 40px; border-radius: 16px; color: white; 
                    margin-bottom: 40px; text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,0.12)'>
            <h1 style='font-size: 3.5rem; margin: 0 0 15px 0; font-weight: 700'>🌱 EcoAgent AI</h1>
            <h3 style='font-weight: 300; margin: 0 0 20px 0; font-size: 1.4rem; opacity: 0.95'>
                Intelligent Sustainability Advisor & Carbon Tracking Platform
            </h3>
            <p style='margin: 0; font-size: 1.1rem; opacity: 0.9; max-width: 800px; margin: 0 auto'>
                Empower yourself to take measurable climate action through AI-driven insights, 
                personalized recommendations, and real-time sustainability analytics.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Quick Start
    st.markdown("""
    <div style='background: #f5f5f5; padding: 25px; border-radius: 12px; margin-bottom: 30px'>
        <h3 style='margin-top: 0; color: #1b5e20'>🚀 Quick Start</h3>
        <p><strong>Get started in 3 easy steps:</strong></p>
        <ol>
            <li><strong>Dashboard:</strong> Enter your consumption data and see your carbon footprint</li>
            <li><strong>AI Advisor:</strong> Get personalized recommendations from our AI</li>
            <li><strong>Reports:</strong> Generate and download your sustainability report</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    # Feature Overview
    st.subheader("📊 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='margin-top: 0; color: #1b5e20'>📊 Analytics Dashboard</h3>
                <p>Real-time carbon footprint tracking with visual breakdowns by electricity, water, and travel.</p>
                <ul style='margin: 10px 0 0 0'>
                    <li>KPI metrics & eco-score</li>
                    <li>Interactive charts</li>
                    <li>Goal tracking</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='margin-top: 0; color: #1b5e20'>🤖 AI Advisor</h3>
                <p>Powered by Google Gemini & RAG technology for personalized sustainability advice.</p>
                <ul style='margin: 10px 0 0 0'>
                    <li>Smart recommendations</li>
                    <li>Knowledge base integration</li>
                    <li>Question answering</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='margin-top: 0; color: #1b5e20'>📄 Bill Analyzer</h3>
                <p>Extract consumption data from utility bills automatically using AI.</p>
                <ul style='margin: 10px 0 0 0'>
                    <li>PDF extraction</li>
                    <li>Auto data population</li>
                    <li>Multiple formats</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Additional Features
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='margin-top: 0; color: #1b5e20'>🎯 Goals & Progress</h3>
                <p>Set and track your sustainability goals with visual progress indicators.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='margin-top: 0; color: #1b5e20'>💡 Eco Tips</h3>
                <p>Personalized and random sustainability tips based on your usage patterns.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='margin-top: 0; color: #1b5e20'>📜 PDF Reports</h3>
                <p>Generate comprehensive reports with your full sustainability analysis.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🌍 UN Sustainable Development Goals")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); 
                        padding: 25px; border-radius: 12px; text-align: center; 
                        border-left: 4px solid #f9a825'>
                <h2 style='color: #e65100; margin: 0 0 10px 0'>⚡</h2>
                <h4 style='margin: 0 0 10px 0; color: #e65100'>SDG 7</h4>
                <p style='margin: 0; color: #666'><b>Affordable & Clean Energy</b></p>
                <p style='margin: 5px 0 0 0; font-size: 0.9rem; color: #999'>
                Promoting energy efficiency through data-backed electricity analysis.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #fff9c4 0%, #fffde7 100%); 
                        padding: 25px; border-radius: 12px; text-align: center; 
                        border-left: 4px solid #fbc02d'>
                <h2 style='color: #f57f17; margin: 0 0 10px 0'>♻️</h2>
                <h4 style='margin: 0 0 10px 0; color: #f57f17'>SDG 12</h4>
                <p style='margin: 0; color: #666'><b>Responsible Consumption</b></p>
                <p style='margin: 5px 0 0 0; font-size: 0.9rem; color: #999'>
                Reducing waste and optimizing water and travel habits.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); 
                        padding: 25px; border-radius: 12px; text-align: center; 
                        border-left: 4px solid #2e7d32'>
                <h2 style='color: #1b5e20; margin: 0 0 10px 0'>🌍</h2>
                <h4 style='margin: 0 0 10px 0; color: #1b5e20'>SDG 13</h4>
                <p style='margin: 0; color: #666'><b>Climate Action</b></p>
                <p style='margin: 5px 0 0 0; font-size: 0.9rem; color: #999'>
                Measuring and mitigating individual carbon contributions.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Stats Section
    st.markdown("""
    <div style='background: #f5f5f5; padding: 30px; border-radius: 12px'>
        <h3 style='margin-top: 0; text-align: center; color: #1b5e20'>🌱 Your Sustainability Journey Starts Here</h3>
        <p style='text-align: center; color: #666; font-size: 1.1rem'>
        Join thousands of users taking action to reduce their carbon footprint and build a sustainable future.
        </p>
        <p style='text-align: center; margin-top: 20px'>
        <strong>👈 Use the sidebar to navigate to different modules or choose from the pages below</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Technology Stack
    st.subheader("🔧 Technology Stack")
    
    st.markdown("""
    | Component | Technology |
    |-----------|-----------|
    | **Frontend** | Streamlit 1.35.0 |
    | **AI Models** | Google Gemini 3.5, Ollama |
    | **Vector DB** | ChromaDB 0.5.0 |
    | **RAG Framework** | LangChain 0.2.1 |
    | **Analytics** | Plotly, NumPy, Pandas |
    | **PDF Processing** | PyMuPDF, PyPDF, ReportLab |
    """)

    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 20px; color: #666; font-size: 0.9rem'>
        <p style='margin: 0'>🌱 <strong>EcoAgent AI</strong> | Sustainability through AI Innovation</p>
        <p style='margin: 10px 0 0 0'>Aligned with UN Sustainable Development Goals 7, 12, and 13</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
