import streamlit as st
import pydeck as pdk

from utils.ui_enhancer import inject_custom_css



st.set_page_config(
    page_title="Global Threat Map",
    page_icon="🌍",
    layout="wide"
)

from utils.data_loader import load_data
df = load_data()


inject_custom_css()

st.title("🌍 3D Global Threat Map")



st.sidebar.header("Filters")

year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["iyear"].unique().tolist())
)

if year != "All":
    df = df[df["iyear"] == year]

df = df.dropna(subset=["latitude", "longitude"])

if len(df) > 50000:
    st.warning(f"Displaying a random sample of 50,000 incidents out of {len(df):,} for 3D map performance.")
    df = df.sample(n=50000, random_state=42)

st.markdown("### 🔴 Incident Density")
st.markdown("Hold **Shift + drag** to rotate the map in 3D.")

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    df,
    get_position=["longitude", "latitude"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
    radius=100000,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=0,
    latitude=20,
    zoom=1.5,
    min_zoom=1,
    max_zoom=15,
    pitch=45,
    bearing=0,
)

# Render
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "Incident Cluster"},
    map_style="mapbox://styles/mapbox/dark-v10"
))

st.info("👈 Change filters from the sidebar.")
