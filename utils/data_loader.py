import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    local_path = "data/globalterrorism.csv"
    
    if not os.path.exists(local_path):
        with st.spinner("Downloading GTD Dataset from Kaggle (First load only)..."):
            import kagglehub
            path = kagglehub.dataset_download("START-UMD/gtd")
            csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
            if csv_files:
                local_path = os.path.join(path, csv_files[0])
            else:
                st.error("No CSV found in downloaded Kaggle dataset.")
                return pd.DataFrame()
            
    df = pd.read_csv(
        local_path,
        encoding="latin1",
        low_memory=False
    )
    df["nkill"] = df["nkill"].fillna(0)
    df["nwound"] = df["nwound"].fillna(0)
    return df
