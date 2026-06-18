"""
Global styling and theme configuration for EcoAgent AI
"""

def inject_custom_css():
    """Inject custom CSS for consistent theming across the app"""
    import streamlit as st
    
    st.markdown("""
    <style>
    /* Primary Colors */
    :root {
        --primary-green: #1b5e20;
        --secondary-green: #2e7d32;
        --light-green: #e8f5e9;
        --accent-green: #4caf50;
        --neutral-gray: #f5f5f5;
        --text-dark: #212121;
        --text-light: #757575;
        --success: #4caf50;
        --warning: #ff9800;
        --danger: #f44336;
    }

    /* Main Content Area */
    .main {
        background-color: #fafafa;
    }

    /* Headers */
    h1, h2, h3 {
        color: var(--primary-green);
        font-weight: 600;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.5rem;
        letter-spacing: -0.5px;
    }

    h2 {
        font-size: 1.8rem;
        margin-top: 30px;
    }

    h3 {
        font-size: 1.3rem;
    }

    /* Cards and Containers */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
    }

    [data-testid="stMetric"]:hover {
        box-shadow: 0 4px 16px rgba(27, 94, 32, 0.12);
        transform: translateY(-2px);
    }

    [data-testid="stColumn"] [data-testid="stMetric"] {
        margin-bottom: 15px;
    }

    /* Buttons */
    .stButton > button {
        background-color: var(--secondary-green);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(46, 125, 50, 0.2);
    }

    .stButton > button:hover {
        background-color: var(--primary-green);
        box-shadow: 0 4px 16px rgba(46, 125, 50, 0.3);
        transform: translateY(-1px);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Info/Warning/Success Boxes */
    .stAlert {
        border-radius: 8px;
        border-left: 4px solid;
        padding: 15px;
        background-color: #fafafa;
    }

    [data-testid="stAlert"] {
        border-radius: 8px;
        padding: 15px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f9f9f9;
    }

    [data-testid="stSidebar"] h2 {
        color: var(--primary-green);
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.1rem;
    }

    [data-testid="stSidebar"] .stNumberInput > div > div > input,
    [data-testid="stSidebar"] .stSelectbox > div > div > select {
        border-radius: 6px;
        border: 1px solid #e0e0e0;
        padding: 8px 12px;
    }

    /* Input Fields */
    input, select, textarea {
        border-radius: 6px !important;
        border: 1px solid #e0e0e0 !important;
        padding: 10px 12px !important;
    }

    input:focus, select:focus, textarea:focus {
        border-color: var(--secondary-green) !important;
        box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1) !important;
    }

    /* Dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #e0e0e0, transparent);
        margin: 25px 0;
    }

    /* Tabs */
    [data-testid="stTabs"] [role="tablist"] button {
        border-radius: 8px 8px 0 0;
        padding: 12px 20px;
        font-weight: 500;
    }

    /* Charts */
    .plotly {
        border-radius: 8px;
        overflow: hidden;
    }

    /* Expanders */
    [data-testid="stExpander"] {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        background-color: #fafafa;
    }

    [data-testid="stExpander"] summary {
        font-weight: 600;
        color: var(--primary-green);
        padding: 12px;
    }

    /* File Uploader */
    .uploadedFile {
        background-color: #e8f5e9;
        border: 2px dashed var(--secondary-green);
        border-radius: 8px;
        padding: 15px;
    }

    /* Metric Values */
    [data-testid="stMetricValue"] {
        font-weight: 700;
        color: var(--primary-green);
        font-size: 1.8rem;
    }

    /* Metric Label */
    [data-testid="stMetricLabel"] {
        color: var(--text-light);
        font-size: 0.9rem;
        font-weight: 500;
    }

    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%);
        color: white;
        padding: 40px;
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 16px rgba(27, 94, 32, 0.2);
    }

    .hero-section h1 {
        color: white;
        margin: 0 0 10px 0;
    }

    .hero-section p {
        margin: 0;
        opacity: 0.95;
        font-size: 1.1rem;
    }

    /* Stats Grid */
    .stat-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        text-align: center;
        transition: all 0.3s ease;
    }

    .stat-card:hover {
        box-shadow: 0 4px 16px rgba(27, 94, 32, 0.15);
        border-color: var(--secondary-green);
    }

    .stat-card .value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--secondary-green);
        margin: 10px 0;
    }

    .stat-card .label {
        font-size: 0.9rem;
        color: var(--text-light);
        font-weight: 500;
    }

    /* Badge Styles */
    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }

    .badge-success {
        background-color: #c8e6c9;
        color: #1b5e20;
    }

    .badge-warning {
        background-color: #ffe0b2;
        color: #e65100;
    }

    .badge-danger {
        background-color: #ffcdd2;
        color: #b71c1c;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        h1 { font-size: 1.8rem; }
        h2 { font-size: 1.3rem; }
        h3 { font-size: 1rem; }
        
        .hero-section {
            padding: 25px;
        }
        
        [data-testid="stMetric"] {
            padding: 15px;
        }
    }

    /* Smooth Transitions */
    * {
        transition: background-color 0.2s ease;
    }

    /* Accessibility */
    :focus-visible {
        outline: 2px solid var(--secondary-green);
        outline-offset: 2px;
    }

    </style>
    """, unsafe_allow_html=True)
