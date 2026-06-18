import streamlit as st
import os
from utils.report_gen import ReportGenerator
from styles import inject_custom_css

# Page Config MUST be first
st.set_page_config(page_title="Reports", layout="wide")

# Apply global CSS
inject_custom_css()

st.markdown("""
    <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 30px'>
        <h1 style='color: white; margin: 0'>📜 Sustainability Reports</h1>
        <p style='margin: 10px 0 0 0; opacity: 0.9'>Generate comprehensive PDF reports of your environmental impact</p>
    </div>
""", unsafe_allow_html=True)

st.info("📊 Generate a detailed PDF report that includes your carbon footprint analysis, eco-score, and personalized AI recommendations aligned with UN SDGs.")

# Check prerequisites
missing_data = []

if not st.session_state.user_data.get('footprint'):
    missing_data.append("Dashboard analysis (enter your consumption data)")

if 'last_advice' not in st.session_state:
    missing_data.append("AI recommendations (generate advice in Sustainability Advisor)")

if missing_data:
    st.warning(f"""
    ⚠️ **Report Data Missing**
    
    To generate a complete report, please first complete:
    """)
    for item in missing_data:
        st.write(f"- [ ] {item}")
    
    st.divider()
    st.markdown("### 📝 Steps to Generate Report")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Step 1: Dashboard**
        1. Go to Dashboard
        2. Enter your data
        3. Click Recalculate
        """)
    
    with col2:
        st.markdown("""
        **Step 2: AI Advisor**
        1. Go to Sustainability Advisor
        2. Click Generate Advice
        3. Review recommendations
        """)
    
    with col3:
        st.markdown("""
        **Step 3: Generate Report**
        1. Return to this page
        2. Click Generate PDF
        3. Download your report
        """)

else:
    st.success("✅ **All data ready!** Your report can now be generated.")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 📋 Report Summary")
        
        fp = st.session_state.user_data['footprint']
        cols = st.columns(4)
        cols[0].metric("Total CO2e", f"{fp['total']:.1f} kg")
        cols[1].metric("Electricity", f"{fp['breakdown'].get('Electricity', 0):.1f} kg")
        cols[2].metric("Water", f"{fp['breakdown'].get('Water', 0):.1f} kg")
        cols[3].metric("Travel", f"{fp['breakdown'].get('Travel', 0):.1f} kg")
    
    with col2:
        if st.button("⚙️ Report Options", use_container_width=True):
            st.session_state.show_options = not st.session_state.get('show_options', False)
    
    st.markdown("---")
    
    report_filename = "EcoAgent_Report.pdf"
    report_path = os.path.join("reports", report_filename)
    
    if st.button("📥 Generate Full PDF Report", use_container_width=True, type="primary"):
        with st.spinner("🔄 Building your comprehensive PDF report..."):
            try:
                if not os.path.exists("reports"):
                    os.makedirs("reports")
                
                ReportGenerator.generate_pdf(
                    st.session_state.user_data,
                    st.session_state.get('last_advice', "No specific advice generated."),
                    report_path
                )
                
                st.success("✅ Report generated successfully!")
                
                # Show download button
                with open(report_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Report PDF",
                        data=f,
                        file_name=report_filename,
                        mime="application/pdf",
                        use_container_width=True
                    )
                
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Error generating report: {str(e)}")
                st.info("Please ensure all required data is available and try again.")
    
    st.markdown("---")
    
    st.subheader("📄 What's Included in Your Report?")
    
    features = [
        ("📊 Carbon Footprint Analysis", "Detailed breakdown of your emissions by category"),
        ("🏆 Sustainability Score", "Your eco-score rating and grade"),
        ("🎯 AI-Generated Recommendations", "Personalized action plan from the advisor"),
        ("📈 Impact Comparison", "How your footprint compares to sustainable targets"),
        ("🌍 UN SDG Alignment", "How your actions contribute to climate goals"),
        ("💡 Actionable Tips", "Specific steps to reduce your environmental impact"),
    ]
    
    for icon, title, desc in [(f[0], f[1], features[i][1]) for i, f in enumerate(features)]:
        st.markdown(f"""
        <div style='background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 10px'>
            <p style='margin: 0'><strong>{icon} {title}</strong></p>
            <p style='margin: 5px 0 0 0; color: #666; font-size: 0.9rem'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("📁 Report History")

if os.path.exists("reports"):
    report_files = [f for f in os.listdir("reports") if f.endswith('.pdf')]
    
    if report_files:
        st.write(f"Found {len(report_files)} report(s)")
        
        for report_file in report_files:
            report_path = os.path.join("reports", report_file)
            file_size = os.path.getsize(report_path) / 1024  # KB
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"📄 **{report_file}**")
            with col2:
                st.caption(f"{file_size:.1f} KB")
            with col3:
                with open(report_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download",
                        f,
                        file_name=report_file,
                        mime="application/pdf",
                        key=report_file
                    )
    else:
        st.info("No reports generated yet. Create one above!")
else:
    st.info("Report history will appear here after you generate your first report.")

