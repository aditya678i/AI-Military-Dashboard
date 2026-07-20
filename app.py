import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from utils.ui_enhancer import inject_custom_css

st.set_page_config(
    page_title="AI Military Intelligence Dashboard",
    page_icon="🛡",
    layout="wide"
)

inject_custom_css()

@st.dialog("Welcome")
def welcome_popup():
    st.markdown("### AI Military Based Project")
    st.markdown("**Name:** Aditya Singh")
    st.markdown("**Enrollment Number:** BSERC-23676")
    st.markdown("**College:** GLA University, Mathura")
    if st.button("Enter Dashboard", use_container_width=True):
        st.session_state.show_popup = False
        st.rerun()

if "show_popup" not in st.session_state:
    st.session_state.show_popup = True

if st.session_state.show_popup:
    welcome_popup()

st.title("🛡 AI-Based Military Intelligence Dashboard")

st.markdown("""
**Created by Aditya Singh**  
**Enrollment Number:** BSERC-23676  
**College:** GLA University, Mathura
""")


st.markdown("""
### Welcome

This dashboard provides military intelligence analysis using the
Global Terrorism Database (GTD).

👈 Select a page from the sidebar.
""")

st.info("""
Available Modules

- 🏠 Home
- 🌍 Global Threat Map
- 🌎 Country Analysis
- 🤖 Attack Prediction
- 🚨 Threat Level Prediction
- 📈 Forecasting
- 🧠 AI Intelligence Report
- 📊 Data Explorer
- ⚙ Settings

👈 Use the **left sidebar** to navigate.
""")

st.info("Select a page from the sidebar to begin.")
