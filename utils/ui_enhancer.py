import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        /* Glassmorphism Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(30, 30, 30, 0.8) !important;
            backdrop-filter: blur(10px) !important;
            border-right: 1px solid rgba(255, 75, 75, 0.3);
        }
        
        /* Metric Cards Hover Effect */
        [data-testid="stMetricValue"] {
            transition: all 0.3s ease-in-out;
            color: #ff4b4b !important;
            font-weight: bold !important;
        }
        [data-testid="stMetric"]:hover [data-testid="stMetricValue"] {
            transform: scale(1.1);
            text-shadow: 0px 0px 15px rgba(255, 75, 75, 0.9);
        }
        
        /* Container Hover Animation */
        div[data-testid="stPlotlyChart"] {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 10px;
        }
        div[data-testid="stPlotlyChart"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 75, 75, 0.15);
        }

        /* Glowing Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #ff4b4b, #b31217) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            font-weight: bold;
        }
        .stButton>button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0px 5px 20px rgba(255, 75, 75, 0.7) !important;
            color: white !important;
        }
        
        /* Headers */
        h1, h2, h3 {
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        h1 {
            border-bottom: 2px solid #ff4b4b;
            padding-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
