import pydeck as pdk
import pandas as pd

df = pd.DataFrame({'latitude': [37.7749], 'longitude': [-122.4194]})
layer = pdk.Layer(
    "HexagonLayer",
    df,
    get_position=["longitude", "latitude"],
    elevation_scale=50,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
)
view_state = pdk.ViewState(longitude=-122.4194, latitude=37.7749, zoom=10, pitch=45)
deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
deck.to_html("test_map.html")
print("Done")
