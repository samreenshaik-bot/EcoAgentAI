import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.calculator import CarbonCalculator
from utils.eco_score import EcoScoreEngine
from utils.goals_tracking import EcoTipsProvider, GoalsManager

# Page Header
st.set_page_config(page_title="EcoAgent Dashboard", layout="wide")

st.markdown("""
    <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 30px'>
        <h1 style='color: white; margin: 0'>🌱 EcoAgent Dashboard</h1>
        <p style='margin: 10px 0 0 0; opacity: 0.9'>Real-time Sustainability Analytics | Aligned with SDG 7, 12 & 13</p>
    </div>
""", unsafe_allow_html=True)

# Shared State Logic
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {
        'inputs': {'elec_kwh': 0.0, 'water_liters': 0.0, 'travel_km': 0.0, 'transport_mode': 'Car'},
        'footprint': None, 'score': None
    }
elif 'inputs' not in st.session_state['user_data']:
    # Migrate old user_data format
    st.session_state['user_data'] = {
        'inputs': {'elec_kwh': 0.0, 'water_liters': 0.0, 'travel_km': 0.0, 'transport_mode': 'Car'},
        'footprint': st.session_state['user_data'].get('footprint'),
        'score': st.session_state['user_data'].get('score')
    }

inputs = st.session_state.user_data.get('inputs', {})
elec = inputs.get('elec_kwh', 0.0)
water = inputs.get('water_liters', 0.0)
travel = inputs.get('travel_km', 0.0)
mode = inputs.get('transport_mode', 'Car')

# Sidebar inputs
with st.sidebar:
    st.header("📍 Personal Metrics")
    st.info("Update your monthly usage below to recalculate your impact.")
    
    elec = st.number_input("Electricity (kWh)", 0.0, value=elec)
    water = st.number_input("Water (Liters)", 0.0, value=water)
    travel = st.number_input("Travel (km)", 0.0, value=travel)
    mode = st.selectbox("Transport Mode", ["Car", "Bus", "Train", "Bike"], index=["Car", "Bus", "Train", "Bike"].index(mode))

    if st.button("🔄 Recalculate Now", use_container_width=True):
        st.session_state.user_data['inputs'] = {'elec_kwh': elec, 'water_liters': water, 'travel_km': travel, 'transport_mode': mode}
        st.session_state.user_data['footprint'] = CarbonCalculator.calculate_total_footprint(elec, water, travel, mode)
        st.session_state.user_data['score'] = EcoScoreEngine.calculate_score(st.session_state.user_data['footprint']['total'])
        st.toast("✅ Analytics Updated!", icon="✨")

# Main Content
if st.session_state.user_data['footprint']:
    fp = st.session_state.user_data['footprint']
    score = st.session_state.user_data['score']

    # Row 1: KPI Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total CO2e", f"{fp['total']:.1f} kg", delta_color="inverse")
    m2.metric("Sustainability Score", f"{score['score']}/100")
    m3.metric("Current Grade", score['grade'])
    m4.metric("Status", score['label'])

    st.markdown("---")

    # Row 2: Visual Charts
    c1, c2 = st.columns([1, 1])

    with c1:
        st.subheader("💡 Impact Breakdown")
        df = pd.DataFrame({
            "Category": list(fp['breakdown'].keys()),
            "Emissions (kg CO2e)": list(fp['breakdown'].values())
        })
        fig = px.pie(df, values='Emissions (kg CO2e)', names='Category', 
                     hole=0.5, color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(
            margin=dict(t=0, b=0, l=0, r=0),
            font=dict(size=11),
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("🏆 Sustainability Gauge")
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score['score'],
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2e7d32"},
                'steps': [
                    {'range': [0, 50], 'color': "#ffebee"},
                    {'range': [50, 80], 'color': "#fff3e0"},
                    {'range': [80, 100], 'color': "#e8f5e9"}
                ],
                'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}
            }
        ))
        fig_gauge.update_layout(margin=dict(t=30, b=0, l=30, r=30), height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)

    st.markdown("---")

    # Row 3: Comparison & Goals
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("📊 vs Global Target")
        target = EcoScoreEngine.MONTHLY_TARGET
        categories = ['Your Impact', 'Sustainable Limit']
        values = [fp['total'], target]
        
        fig_bar = px.bar(x=categories, y=values, color=categories, 
                         color_discrete_map={'Your Impact': '#81c784', 'Sustainable Limit': '#2e7d32'},
                         labels={'x': 'Category', 'y': 'kg CO2e'})
        fig_bar.update_layout(
            showlegend=False,
            margin=dict(t=30, b=0, l=0, r=0)
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with c2:
        st.subheader("🎯 Progress to Goals")
        
        goals_data = GoalsManager.get_all_goals()
        monthly_target = goals_data.get('monthly_target', 100)
        
        progress_pct = max(0, (monthly_target - fp['total']) / monthly_target * 100)
        
        st.metric("Distance from Target", f"{max(0, monthly_target - fp['total']):.1f} kg CO2e to save", 
                 delta=f"{progress_pct:.1f}%" if progress_pct < 100 else "Target exceeded ⚠️")
        
        st.progress(min(progress_pct / 100, 1.0))
        
        if progress_pct >= 80:
            st.success("🎉 Great! You're close to your target!")
        elif progress_pct >= 50:
            st.info("💪 Keep going! You're on track.")
        else:
            st.warning("⚠️ More reductions needed to hit your target.")

    st.markdown("---")

    # Row 4: Quick Tips
    st.subheader("💡 Quick Tips for You")
    
    tips = EcoTipsProvider.get_personalized_tips(fp['breakdown'])
    
    tip_cols = st.columns(len(tips[:3]))
    for i, (col, tip) in enumerate(zip(tip_cols, tips[:3])):
        with col:
            st.markdown(f"""
            <div style='background: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #2e7d32'>
                <p style='margin: 0; font-size: 0.9rem'>{tip['tip']}</p>
                <small style='color: #666'>Impact: {tip['impact']}</small>
            </div>
            """, unsafe_allow_html=True)

else:
    st.markdown("""
        <div style='text-align: center; padding: 50px'>
            <h2 style='color: #666'>No Data Analyzed Yet</h2>
            <p>Please enter your consumption details in the sidebar to generate your sustainability profile.</p>
        </div>
    """, unsafe_allow_html=True)
