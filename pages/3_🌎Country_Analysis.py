import streamlit as st
import plotly.express as px
import pydeck as pdk
from utils.data_loader import load_data
from utils.ui_enhancer import inject_custom_css

st.set_page_config(
    page_title="Country Analysis",
    page_icon="🌎",
    layout="wide"
)

inject_custom_css()

st.title("🌎 Country Analysis")

df = load_data()

# -----------------------------
# Sidebar
# -----------------------------

countries = sorted(df["country_txt"].dropna().unique())

country = st.sidebar.selectbox(
    "Select Country",
    countries
)

country_df = df[df["country_txt"] == country]

st.header(f"Intelligence Report : {country}")

# -----------------------------
# KPIs
# -----------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Incidents",
    f"{len(country_df):,}"
)

c2.metric(
    "Fatalities",
    int(country_df["nkill"].sum())
)

c3.metric(
    "Injured",
    int(country_df["nwound"].sum())
)

c4.metric(
    "Groups",
    country_df["gname"].nunique()
)

st.divider()

# -----------------------------
# Attacks Over Time
# -----------------------------

left, right = st.columns(2)

with left:

    yearly = (
        country_df
        .groupby("iyear")
        .size()
        .reset_index(name="Attacks")
    )

    fig = px.line(
        yearly,
        x="iyear",
        y="Attacks",
        markers=True,
        title="Attacks Over Years",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    attack = (
        country_df
        .groupby("attacktype1_txt")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        attack,
        names="attacktype1_txt",
        values="Count",
        title="Attack Types",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------------
# Organizations
# -----------------------------

left, right = st.columns(2)

with left:

    groups = (
        country_df
        .groupby("gname")
        .size()
        .reset_index(name="Attacks")
        .sort_values("Attacks", ascending=False)
        .head(10)
    )

    fig = px.bar(
        groups,
        x="Attacks",
        y="gname",
        orientation="h",
        title="Top Terrorist Organizations",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    weapon = (
        country_df
        .groupby("weaptype1_txt")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
    )

    fig = px.bar(
        weapon,
        x="weaptype1_txt",
        y="Count",
        title="Weapon Types",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------------
# Incident Map (3D)
# -----------------------------

st.subheader("3D Incident Locations")
st.markdown("Hold **Shift + drag** to rotate the map in 3D.")

map_df = country_df.dropna(
    subset=["latitude", "longitude"]
)

if len(map_df) > 10000:
    st.warning(f"Displaying a random sample of 10,000 incidents out of {len(map_df):,} to improve map performance.")
    map_df = map_df.sample(n=10000, random_state=42)

avg_lat = map_df["latitude"].mean() if not map_df.empty else 0
avg_lon = map_df["longitude"].mean() if not map_df.empty else 0

layer = pdk.Layer(
    "ColumnLayer",
    data=map_df,
    get_position=["longitude", "latitude"],
    get_elevation="nkill",
    elevation_scale=1000,
    radius=5000,
    get_fill_color=[255, 75, 75, 180],
    pickable=True,
    auto_highlight=True,
)

view_state = pdk.ViewState(
    longitude=avg_lon,
    latitude=avg_lat,
    zoom=4,
    min_zoom=1,
    max_zoom=15,
    pitch=45,
    bearing=0,
)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{city}\nFatalities: {nkill}"},
    map_style="mapbox://styles/mapbox/dark-v10"
))

st.divider()

# -----------------------------
# Incident Table
# -----------------------------

st.subheader("Incident Details")

cols = [
    "iyear",
    "city",
    "attacktype1_txt",
    "targtype1_txt",
    "weaptype1_txt",
    "gname",
    "nkill",
    "nwound"
]

st.dataframe(
    country_df[cols],
    use_container_width=True
)

# -----------------------------
# Download
# -----------------------------

csv = country_df.to_csv(
    index=False
).encode()

st.download_button(
    "Download Country Data",
    csv,
    file_name=f"{country}.csv",
    mime="text/csv"
)
