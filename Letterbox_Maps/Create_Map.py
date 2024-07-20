import os
import random
import folium
import geopandas as gpd

def add_layer_to_map(gdf, m, layer_name, color=None):
    """Add a GeoDataFrame as a layer to the Folium map with a specified color."""
    if color is None:
        color = "#%06x" % random.randint(0, 0xFFFFFF)
    
    layer = folium.FeatureGroup(name=layer_name)

    # Add GeoJson with popups
    for index, row in gdf.iterrows():
        folium.GeoJson(
            row['geometry'],
            style_function=lambda x, color=color: {'color': color},
        ).add_to(layer)
    
    layer.add_to(m)

# List all files in the folder
folder_path = "Letterbox_Maps/GeoJSON/Zone_1"
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

output_html = "Letterbox_Maps/Zone_1_map.html"

# Create a folium map
m = folium.Map(location=(-32.9, 151.79), zoom_start=11)

for suburb in files:
    gdf = gpd.read_file(os.path.join(folder_path, suburb))
    gdf = gdf.drop(columns=['osmid', 'length'])
    # Convert lists in the 'highway' column to strings
    #area['osmid'] = area['osmid'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    if 'highway' in gdf.columns:
        gdf['highway'] = gdf['highway'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        gdf = gdf[gdf.highway == "residential"]
    #if 'name' in gdf.columns:
        #gdf['name'] = gdf['name'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        #gdf = gdf[gdf.highway == "residential"]
    add_layer_to_map(gdf, m, suburb)

folium.LayerControl().add_to(m)

m.save(output_html)
