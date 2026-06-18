import streamlit as st
from utils.pdf_extractor import BillExtractor
from styles import inject_custom_css

# Page Config MUST be first
st.set_page_config(page_title="Bill Analyzer", layout="wide")

# Apply global CSS
inject_custom_css()

st.markdown("""
    <div style='background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 30px'>
        <h1 style='color: white; margin: 0'>📄 Smart Bill Analyzer</h1>
        <p style='margin: 10px 0 0 0; opacity: 0.9'>Upload bills to auto-extract consumption data and track your usage</p>
    </div>
""", unsafe_allow_html=True)

st.info("💡 Upload your utility bills (electricity, water) and we'll automatically extract consumption data to update your dashboard.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
        <h3 style='color: #1b5e20; margin-top: 0'>⚡ Electricity Bill</h3>
        <p style='color: #666; margin: 0'>Extract kWh consumption</p>
    </div>
    """, unsafe_allow_html=True)
    
    elec_file = st.file_uploader("Upload Electricity PDF", type=['pdf'], key='elec')
    if elec_file:
        with st.spinner("🔍 Extracting data from PDF..."):
            val, text = BillExtractor.process_bill(elec_file, 'electricity')
            if val:
                st.success(f"✅ Found: **{val:.1f} kWh**")
                
                # Show preview
                with st.expander("👁️ Preview extracted text"):
                    st.text(text[:500] + "..." if len(text) > 500 else text)
                
                if st.button("➕ Apply to Dashboard", use_container_width=True, key='apply_elec'):
                    st.session_state.user_data['inputs']['elec_kwh'] = val
                    st.success("✨ Electricity data updated in Dashboard!")
                    st.balloons()
            else:
                st.warning("❌ Could not auto-extract kWh. The PDF format might be unsupported.")
                st.info("**Supported formats:** PDFs with visible text (not scanned images)")

with col2:
    st.markdown("""
    <div style='background: #e8f5e9; padding: 20px; border-radius: 12px; border-left: 4px solid #2e7d32'>
        <h3 style='color: #1b5e20; margin-top: 0'>💧 Water Bill</h3>
        <p style='color: #666; margin: 0'>Extract liters consumption</p>
    </div>
    """, unsafe_allow_html=True)
    
    water_file = st.file_uploader("Upload Water PDF", type=['pdf'], key='water')
    if water_file:
        with st.spinner("🔍 Extracting data from PDF..."):
            val, text = BillExtractor.process_bill(water_file, 'water')
            if val:
                st.success(f"✅ Found: **{val:.1f} Liters**")
                
                # Show preview
                with st.expander("👁️ Preview extracted text"):
                    st.text(text[:500] + "..." if len(text) > 500 else text)
                
                if st.button("➕ Apply to Dashboard", use_container_width=True, key='apply_water'):
                    st.session_state.user_data['inputs']['water_liters'] = val
                    st.success("✨ Water data updated in Dashboard!")
                    st.balloons()
            else:
                st.warning("❌ Could not auto-extract liters. The PDF format might be unsupported.")
                st.info("**Supported formats:** PDFs with visible text (not scanned images)")

st.markdown("---")

st.subheader("🔧 How It Works")
cols = st.columns(3)

with cols[0]:
    st.markdown("""
    <div style='text-align: center'>
        <h3 style='color: #2e7d32; font-size: 2rem'>1️⃣</h3>
        <p style='color: #666'><strong>Upload PDF</strong></p>
        <p style='font-size: 0.9rem; color: #999'>Choose an electricity or water bill</p>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div style='text-align: center'>
        <h3 style='color: #2e7d32; font-size: 2rem'>2️⃣</h3>
        <p style='color: #666'><strong>Extract Data</strong></p>
        <p style='font-size: 0.9rem; color: #999'>AI finds consumption values</p>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div style='text-align: center'>
        <h3 style='color: #2e7d32; font-size: 2rem'>3️⃣</h3>
        <p style='color: #666'><strong>Apply to Dashboard</strong></p>
        <p style='font-size: 0.9rem; color: #999'>Update your metrics instantly</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("📋 Supported Bill Formats")

format_info = """
| Bill Type | Supported? | Keywords Detected |
|-----------|-----------|-------------------|
| **Electricity** | ✅ Yes | kWh, Units, Consumption, Usage |
| **Water** | ✅ Yes | Liters, m³, Water Units, Volume |
| **Gas** | 🔄 Coming | Therms, m³, Gas Units |
| **Internet** | ❌ No | Not supported yet |

**Note:** Works best with digital PDFs. Scanned images may not extract correctly.
"""

st.markdown(format_info)

st.markdown("---")

with st.expander("⚙️ Settings"):
    st.write("**Data Privacy**")
    st.info("📍 All bill data is processed locally and never stored on external servers.")
    
    if st.button("Clear Uploaded Files", use_container_width=True):
        st.success("✅ Temporary files cleared")
