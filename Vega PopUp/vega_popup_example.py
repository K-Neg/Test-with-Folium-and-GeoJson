import json
import numpy as np

import folium
from folium import Vega
import vincent

scatter_points = {
    'x': np.random.uniform(size=(100,)),
    'y': np.random.uniform(size=(100,)),
}

# Let's create the vincent chart.
scatter_chart = vincent.Scatter(scatter_points,
                                iter_idx='x',
                                width=600,
                                height=300)

# Let's convert it to JSON.
scatter_json = scatter_chart.to_json()

# Let's convert it to dict.
scatter_dict = json.loads(scatter_json)

m = folium.Map([43, -100], zoom_start=4)

popup = folium.Popup()
folium.Vega(scatter_chart, height=350, width=650).add_to(popup)
folium.Marker([30, -120], popup=popup).add_to(m)

# Let's create a Vega popup based on scatter_json.
popup = folium.Popup(max_width=0)
folium.Vega(scatter_json, height=350, width=650).add_to(popup)
folium.Marker([30, -100], popup=popup).add_to(m)

# Let's create a Vega popup based on scatter_dict.
popup = folium.Popup(max_width=650)
folium.Vega(scatter_dict, height=350, width=650).add_to(popup)
folium.Marker([30, -80], popup=popup).add_to(m)

m.save('vega_popups.html')
