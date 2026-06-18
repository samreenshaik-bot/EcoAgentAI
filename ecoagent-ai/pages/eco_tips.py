import streamlit as st
from utils.goals_tracking import EcoTipsProvider
import random

st.set_page_config(page_title="Eco Tips & Advice", layout="wide")

st.markdown("""
    <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 30px'>
        <h1 style='color: white; margin: 0'>💡 Eco Tips & Advice</h1>
        <p style='margin: 10px 0 0 0; opacity: 0.9'>Actionable sustainability tips to reduce your carbon footprint</p>
    </div>
""", unsafe_allow_html=True)

st.info("🌍 Implement these tips to make a real impact on your carbon footprint and the environment!")

# Tabs
tab1, tab2 = st.tabs(["🎯 Personalized Tips", "💡 Random Tips"])

with tab1:
    st.subheader("Tips Based on Your Usage")
    
    if st.session_state.user_data.get('footprint'):
        breakdown = st.session_state.user_data['footprint'].get('breakdown', {})
        
        if breakdown:
            tips = EcoTipsProvider.get_personalized_tips(breakdown)
            
            cols = st.columns(1)
            for i, tip in enumerate(tips):
                st.markdown(f"""
                <div style='background: #e8f5e9; border-left: 4px solid #2e7d32; padding: 20px; border-radius: 8px; margin-bottom: 15px'>
                    <h4 style='margin: 0 0 10px 0; color: #1b5e20'>{tip['tip']}</h4>
                    <div style='display: flex; justify-content: space-between; align-items: center'>
                        <span style='color: #666; font-size: 0.9rem'>Impact Level: <strong>{tip['impact']}</strong></span>
                        <span style='font-size: 1.2rem'>⭐</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No usage data available. Complete the Dashboard analysis first!")
    else:
        st.warning("⚠️ Please fill in your data in the **Dashboard** to get personalized tips.")

with tab2:
    st.subheader("Daily Eco Tips")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.write("Get inspired with random sustainability tips from our database")
    
    with col2:
        if st.button("🔄 Get New Tips", use_container_width=True):
            st.rerun()
    
    tips = EcoTipsProvider.get_random_tips(limit=5)
    
    for i, tip in enumerate(tips, 1):
        impact_color = {
            "High": "#4caf50",
            "Medium": "#ff9800",
            "Low": "#f44336"
        }.get(tip.get('impact'), "#2e7d32")
        
        st.markdown(f"""
        <div style='background: white; border: 2px solid {impact_color}; padding: 20px; border-radius: 8px; margin-bottom: 15px'>
            <div style='display: flex; justify-content: space-between; align-items: start'>
                <div style='flex: 1'>
                    <h4 style='margin: 0 0 10px 0; color: #1b5e20'>{i}. {tip['tip']}</h4>
                    <div style='display: flex; gap: 10px'>
                        <span style='background: {impact_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600'>
                            {tip.get('impact', 'Medium')} Impact
                        </span>
                        <span style='background: #e8f5e9; color: #1b5e20; padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600'>
                            {tip.get('category', 'general').replace('_', ' ').title()}
                        </span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("📚 Quick Facts")

facts = [
    "🌳 One tree absorbs approximately 48 lbs of carbon dioxide per year",
    "🚴 Biking for 30 minutes instead of driving saves 4.6 metric tons of CO2 annually",
    "💡 LED bulbs use 75% less energy than incandescent bulbs",
    "💧 Fixing a leaky faucet can save 3,000 gallons of water annually",
    "🚌 Public transportation reduces carbon emissions by 45% compared to driving",
]

fact_cols = st.columns(1)
for fact in facts:
    st.markdown(f"""
    <div style='background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 10px'>
        <p style='margin: 0; color: #1b5e20; font-weight: 500'>{fact}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("🌍 Share Your Sustainability Journey")

col1, col2 = st.columns(2)

with col1:
    if st.button("📸 Take a Sustainability Action Photo", use_container_width=True):
        st.info("Share how you're taking action! (Feature coming soon)")

with col2:
    if st.button("🤝 Compare with Friends", use_container_width=True):
        st.info("Connect and compare your footprints with friends! (Feature coming soon)")
