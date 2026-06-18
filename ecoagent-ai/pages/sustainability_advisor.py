import streamlit as st
from ai.ai_client import AIClient
from ai.rag_pipeline import RAGPipeline
from ai.recommender import SustainabilityRecommender
from styles import inject_custom_css

# Page Config MUST be first after imports
st.set_page_config(page_title="Sustainability Advisor", layout="wide")

# Apply global CSS
inject_custom_css()

st.markdown("""
    <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 30px'>
        <h1 style='color: white; margin: 0'>🤖 AI Sustainability Advisor</h1>
        <p style='margin: 10px 0 0 0; opacity: 0.9'>Get personalized recommendations powered by AI and sustainability knowledge</p>
    </div>
""", unsafe_allow_html=True)

# lazy init AI
if 'ai_client' not in st.session_state:
    st.session_state.ai_client = AIClient()
if 'rag_pipeline' not in st.session_state:
    st.session_state.rag_pipeline = RAGPipeline()

# Initialize user_data if not present
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'footprint': 0,
        'electricity': 0,
        'gas': 0,
        'water': 0,
        'waste': 0,
        'travel': 0
    }

# Create tabs
tab1, tab2, tab3 = st.tabs(["📋 Personalized Plan", "💬 Ask Questions", "⚙️ Settings"])

with tab1:
    # User Data Check
    if not st.session_state.user_data.get('footprint'):
        st.warning("""
        ⚠️ **Please complete your profile first!**
        
        1. Go to the **Dashboard** page
        2. Enter your electricity, water, and travel data
        3. Click "Recalculate Now"
        4. Return here for personalized advice
        """)
    else:
        data = st.session_state.user_data
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader("Your Current Profile")
            profile_cols = st.columns(3)
            profile_cols[0].metric("💡 Electricity", f"{data.get('electricity', 0):.0f} kWh", label_visibility="collapsed")
            profile_cols[1].metric("💧 Water", f"{data.get('water', 0):.0f} L", label_visibility="collapsed")
            profile_cols[2].metric("🚗 Travel", f"{data.get('travel', 0):.0f} km", label_visibility="collapsed")
        
        with col2:
            st.markdown("")
            st.markdown("")
            if st.button("🔄 Refresh Data", use_container_width=True):
                st.rerun()
        
        st.markdown("---")
        
        if st.button("✨ Generate Personalized Advice", use_container_width=True):
            with st.spinner("🤔 Analyzing your sustainability profile..."):
                advice = SustainabilityRecommender.get_advice(
                    data, 
                    st.session_state.ai_client, 
                    st.session_state.rag_pipeline
                )
                st.session_state.last_advice = advice
                st.toast("✅ Advice generated!", icon="🎉")
                
        if 'last_advice' in st.session_state:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); padding: 25px; border-radius: 12px; border-left: 4px solid #2e7d32'>
                <h3 style='color: #1b5e20; margin-top: 0'>🌿 Your Personalized Action Plan</h3>
                <div style='color: #333; line-height: 1.8'>
            """, unsafe_allow_html=True)
            st.markdown(st.session_state.last_advice)
            st.markdown("</div></div>", unsafe_allow_html=True)

with tab2:
    st.subheader("💬 Ask the Sustainability Expert")
    st.markdown("Ask anything about sustainability, carbon reduction, or eco-friendly practices.")
    
    user_query = st.text_area(
        "Your Question",
        placeholder="e.g., 'What's the most effective way to reduce my electricity consumption?' or 'How does solar energy work?'",
        height=100
    )
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        submit_button = st.button("🔍 Get Answer", use_container_width=True, key="submit_query")
    with col2:
        if st.button("🔄 Clear", use_container_width=True, key="clear_query"):
            st.rerun()
    
    if user_query and submit_button:
        with st.spinner("🔍 Searching knowledge base..."):
            try:
                response = st.session_state.rag_pipeline.query(user_query, st.session_state.ai_client)
                
                st.markdown("""
                <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32; margin-top: 20px'>
                    <h4 style='color: #1b5e20; margin-top: 0'>🤖 Advisor Response</h4>
                    <div style='color: #333; line-height: 1.8'>
                """, unsafe_allow_html=True)
                st.markdown(response)
                st.markdown("</div></div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"⚠️ Error getting response: {str(e)}")
                st.info("💡 Tip: Make sure your knowledge base PDFs are in the `knowledge_base/` folder")

with tab3:
    st.subheader("⚙️ Settings & Maintenance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Knowledge Base Management**")
        if st.button("🔨 Rebuild Knowledge Index", use_container_width=True):
            with st.spinner("📚 Scanning PDFs in knowledge_base/..."):
                try:
                    st.session_state.rag_pipeline.rebuild_index()
                    st.success("✅ Knowledge index rebuilt successfully!")
                    st.info("Your AI advisor now has access to the latest sustainability knowledge from your PDFs.")
                except Exception as e:
                    st.error(f"Error rebuilding index: {str(e)}")
    
    with col2:
        st.markdown("**AI Model Settings**")
        model_info = st.radio("Select AI Provider", ["Google Gemini (Recommended)", "Ollama (Local)"])
        st.caption("Provider being used for generating advice")

st.markdown("---")

st.markdown("""
<div style='background: #f5f5f5; padding: 15px; border-radius: 8px; margin-top: 20px'>
    <h4 style='margin-top: 0'>💡 Tips for Better Advice</h4>
    <ul style='margin: 0; padding-left: 20px'>
        <li>Fill in complete data in the Dashboard for more personalized recommendations</li>
        <li>Ask specific questions about areas where you want to improve</li>
        <li>Add PDF documents to knowledge_base/ for custom sustainability knowledge</li>
        <li>Check back regularly to track your progress and get new recommendations</li>
    </ul>
</div>
""", unsafe_allow_html=True)

