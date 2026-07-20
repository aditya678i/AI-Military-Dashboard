# 🛡️ AI Military Intelligence Dashboard

**Created by:** Aditya Singh  
**Enrollment Number:** BSERC-23676  
**College:** GLA University, Mathura  

## 📖 Overview
The **AI Military Intelligence Dashboard** is an advanced, 3D-interactive, AI-powered command center built to analyze and predict global terrorism threats. Leveraging the **Global Terrorism Database (GTD)** from Kaggle (containing over 180,000 incidents), this project visualizes historical attack patterns, provides deep country-specific intelligence, and utilizes a **Random Forest Classifier** to predict potential threat levels and attack types.

## ✨ Key Features
- **🌍 3D Global Threat Map:** Visualize attack density and high-risk zones using interactive 3D Hexagon PyDeck layers.
- **🌎 Country Analysis:** Dive deep into specific nations with 3D Incident location columns, identifying top terrorist organizations and weapon choices.
- **🤖 AI Attack Prediction:** A trained Machine Learning model (`scikit-learn`) predicts the exact type of attack based on geographical and target data.
- **🚨 Threat Level Prediction:** Classifies the severity (Low, Medium, High, Critical) of potential threats using AI.
- **📈 Forecasting & AI Intelligence:** Beautiful `plotly_dark` charts mapping out trends across decades.
- **🎨 Custom Premium UI:** Built with custom CSS featuring glassmorphism, hover animations, glowing elements, and a classified dark military theme.

## 🛠️ Technology Stack
- **Frontend/UI:** Streamlit (Python)
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Random Forest)
- **Visualizations:** Plotly, PyDeck (Deck.gl)
- **Data Sourcing:** KaggleHub API

## 🚀 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the data downloader to fetch the real GTD dataset from Kaggle:
   ```bash
   python download_kaggle_data.py
   ```
4. Train the AI prediction models:
   ```bash
   python train_attack_model.py
   ```
5. Launch the Streamlit Dashboard:
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure
```text
project/
│
├── app.py                         # Main Streamlit App Entrypoint
├── train_attack_model.py          # Machine Learning Training Script
├── download_kaggle_data.py        # Kaggle API Data Fetcher
├── requirements.txt               # Python Dependencies
├── utils/
│   ├── data_loader.py             # Data loading and caching utility
│   └── ui_enhancer.py             # Custom CSS and Animation scripts
├── pages/                         # Streamlit Dashboard Modules
│   ├── 1_🏠 Home.py
│   ├── 2_🌍 Global_Threat_Map.py
│   ├── 3_🌎Country_Analysis.py
│   ├── 4_🤖 Attack_Prediction.py
│   ├── 5_🚨Threat_Level.py
│   ├── 6_📈Forecasting.py
│   ├── 7_🧠 AI_Intelligence.py
│   ├── 8_📊Data_Explorer.py
│   └── 9_⚙ Setting.py
├── models/                        # Serialized Joblib ML Models
└── data/                          # Downloaded Kaggle Datasets
```
