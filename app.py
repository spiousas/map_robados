import folium
import os
import pandas as pd
import json

# GeoJson data
provincia_geo = os.path.join('data', 'provincia.json')

with open(provincia_geo) as f:
    geojson_provincia = json.load(f)

# Robos data
provincia_data = os.path.join('data', 'robados_por_provincia.csv')
data = pd.read_csv(provincia_data, na_values=[' '])

# Folium map
coords_Arg = [-37, -66]
map = folium.Map(location=coords_Arg, style="Mapbox Bright",
                 zoom_start=4, control_scale=True, tiles='CartoDB Positron')

folium.Choropleth(
    geo_data = geojson_provincia,
    name = 'Robos totales por provincia 2018/19',
    data = data,
    columns = ['nam', 'Patentados'],
    key = "features.properties.nam",
    fill_color='YlOrRd',
    nan_fill_color = 'red',
    fill_opacity=.7,
    line_opacity=.5,
    highlight=True,
    reset=True
).add_to(map)

map.save('index.html')
