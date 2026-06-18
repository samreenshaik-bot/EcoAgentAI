import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.goals_tracking import GoalsManager, EcoTipsProvider, AchievementBadges
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Goals & Progress", layout="wide")

st.markdown("""
    <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 30px'>
        <h1 style='color: white; margin: 0'>🎯 Goals & Progress Tracking</h1>
        <p style='margin: 10px 0 0 0; opacity: 0.9'>Set targets, track progress, and achieve your sustainability goals</p>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if 'goals_manager' not in st.session_state:
    st.session_state.goals_manager = GoalsManager()

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["📊 Progress", "🎯 Goals", "🏆 Achievements"])

with tab1:
    st.subheader("Your Carbon Footprint Progress")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        monthly_target = st.number_input("Monthly Target (kg CO2e)", value=100, min_value=10)
        if st.button("Set Monthly Target"):
            GoalsManager.set_monthly_target(monthly_target)
            st.success(f"✅ Monthly target set to {monthly_target} kg CO2e")
    
    with col2:
        annual_target = st.number_input("Annual Target (kg CO2e)", value=1200, min_value=100)
        if st.button("Set Annual Target"):
            GoalsManager.set_annual_target(annual_target)
            st.success(f"✅ Annual target set to {annual_target} kg CO2e")
    
    with col3:
        if st.session_state.user_data.get('footprint'):
            footprint = st.session_state.user_data['footprint']['total']
            progress = (monthly_target - footprint) / monthly_target * 100 if monthly_target > 0 else 0
            
            st.metric("Progress to Target", f"{max(0, progress):.1f}%", 
                     delta=f"{footprint:.1f} kg" if footprint else "Add data")
    
    st.markdown("---")
    
    # Progress visualization
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 Monthly Comparison")
        
        # Create sample data for demonstration
        months = pd.date_range(end=datetime.now(), periods=6, freq='ME')
        sample_data = pd.DataFrame({
            'Month': months.strftime('%B'),
            'Your Footprint': [145, 138, 132, 125, 120, 115],
            'Target': [100, 100, 100, 100, 100, 100]
        })
        
        fig = px.line(sample_data, x='Month', y=['Your Footprint', 'Target'],
                     markers=True, 
                     color_discrete_map={'Your Footprint': '#2e7d32', 'Target': '#90ee90'})
        fig.update_layout(
            title="Footprint Trend vs Target",
            yaxis_title="kg CO2e",
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Reduction Metrics")
        
        baseline = 150  # Example baseline
        current = 115   # Example current
        reduction = ((baseline - current) / baseline) * 100
        
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=reduction,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Reduction %"},
            delta={'reference': 0},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2e7d32"},
                'steps': [
                    {'range': [0, 25], 'color': "#ffebee"},
                    {'range': [25, 50], 'color': "#fff3e0"},
                    {'range': [50, 100], 'color': "#e8f5e9"}
                ]
            }
        ))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)

with tab2:
    st.subheader("Your Sustainability Goals")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("**Set a new goal to track your progress**")
        goal_title = st.text_input("Goal Title", placeholder="e.g., Reduce electricity by 20%")
        goal_reduction = st.slider("Target Reduction %", 0, 100, 20)
        goal_deadline = st.date_input("Deadline")
        
        if st.button("Add Goal", use_container_width=True):
            if goal_title:
                GoalsManager.add_goal(goal_title, goal_reduction, goal_deadline.isoformat())
                st.success(f"✅ Goal '{goal_title}' created!")
            else:
                st.error("Please enter a goal title")
    
    with col2:
        st.info("💡 Set realistic goals that are achievable within your deadline")
    
    st.markdown("---")
    
    st.subheader("Active Goals")
    goals_data = GoalsManager.get_all_goals()
    
    if goals_data['goals']:
        for goal in goals_data['goals']:
            with st.expander(f"🎯 {goal['title']} - {goal['target_reduction']}% reduction"):
                col1, col2, col3 = st.columns(3)
                col1.metric("Target Reduction", f"{goal['target_reduction']}%")
                col2.metric("Deadline", goal['deadline'])
                col3.metric("Status", goal['status'].capitalize())
                
                progress_bar = st.progress(0.5)
                st.caption("Progress: 50% complete")
    else:
        st.info("No goals yet. Create one above to get started!")

with tab3:
    st.subheader("🏆 Your Achievements")
    
    # Get earned badges
    earned_badges = AchievementBadges.check_achievements(st.session_state.user_data)
    badges = AchievementBadges.BADGES
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Earned Badges**")
        if earned_badges:
            for badge_key in earned_badges:
                badge = badges.get(badge_key)
                if badge:
                    st.markdown(f"""
                    <div style='background: #e8f5e9; padding: 15px; border-radius: 8px; margin-bottom: 10px'>
                        <h3 style='margin: 0'>{badge['icon']} {badge['name']}</h3>
                        <p style='margin: 5px 0 0 0; color: #666'>{badge['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Complete your first carbon footprint calculation to earn your first badge!")
    
    with col2:
        st.write("**Upcoming Badges**")
        locked_badges = set(badges.keys()) - set(earned_badges)
        for badge_key in list(locked_badges)[:3]:
            badge = badges.get(badge_key)
            if badge:
                st.markdown(f"""
                <div style='background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 10px; opacity: 0.7'>
                    <h3 style='margin: 0'>🔒 {badge['name']}</h3>
                    <p style='margin: 5px 0 0 0; color: #999'>{badge['description']}</p>
                </div>
                """, unsafe_allow_html=True)
