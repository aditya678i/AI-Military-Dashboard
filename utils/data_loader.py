import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    csv_path = "data/globalterrorism.csv"
    if not os.path.exists(csv_path):
        import kagglehub
        import shutil
        path = kagglehub.dataset_download("START-UMD/gtd")
        for file in os.listdir(path):
            if file.endswith(".csv"):
                os.makedirs("data", exist_ok=True)
                shutil.copy(os.path.join(path, file), csv_path)
                break
    
    use_cols = [
        'iyear', 'country_txt', 'region_txt', 'city', 'latitude', 'longitude',
        'attacktype1_txt', 'targtype1_txt', 'weaptype1_txt', 'gname', 'nkill', 'nwound'
    ]
    
    df = pd.read_csv(
        csv_path,
        encoding="latin1",
        usecols=use_cols,
        low_memory=False
    )
    df["nkill"] = df["nkill"].fillna(0)
    df["nwound"] = df["nwound"].fillna(0)
    return df
