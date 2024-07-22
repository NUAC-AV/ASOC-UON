import folium
import osmnx as ox
import geopandas as gpd
import pandas as pd
from folium.plugins import TreeLayerControl

class MapWithTreeLayerControl:
    def __init__(self, base_places, map_location=(-32.9, 151.79), zoom_start=12):
        self.base_places = base_places
        self.map_location = map_location
        self.zoom_start = zoom_start
        self.regions = self._geocode_places()
        self.map = folium.Map(location=self.map_location, zoom_start=self.zoom_start)
        self.colours = [
            'black', 'gray', 'blue', 'darkred', 'lightgreen', 'purple', 'red',
            'green', 'white', 'darkblue', 'darkpurple', 'cadetblue', 'orange',
            'pink', 'lightgray', 'darkgreen'
        ]
        self.overlay_tree = {"label": "Regions and Suburbs", "select_all_checkbox": "Un/select all", "children": []}
    
    def _geocode_places(self):
        regions = []
        for base_group in self.base_places:
            places = [f"{place}, Newcastle, Australia" for place in base_group]
            region = ox.geocode_to_gdf(places)
            regions.append(region)
        return regions
    
    def _add_layers(self):
        for i, region in enumerate(self.regions):
            region_label = f"Region {i+1}"
            region_children = []
            
            for j, (index, row) in enumerate(region.iterrows()):
                suburb_name = row['display_name']
                suburb_layer = folium.FeatureGroup(name=suburb_name, show=False)
                
                folium.GeoJson(
                    row['geometry'],
                    style_function=lambda x, color=self.colours[j % len(self.colours)]: {'color': color},
                    name=suburb_name
                ).add_to(suburb_layer)
                
                suburb_layer.add_to(self.map)
                region_children.append({"label": suburb_name, "layer": suburb_layer})

            self.overlay_tree["children"].append({"label": region_label, "select_all_checkbox": True, "children": region_children})
    
    def add_tree_layer_control(self):
        self._add_layers()
        tree_control = TreeLayerControl(
            base_tree=None,
            overlay_tree=self.overlay_tree,
            closed_symbol='+',
            opened_symbol='-',
            space_symbol='&nbsp;',
            selector_back=False,
            named_toggle=False,
            collapse_all='Collapse all',
            expand_all='Expand all',
            label_is_selector='both'
        )
        tree_control.add_to(self.map)
    
    def save_map(self, output_html):
        self.map.save(output_html)
    
    def display_map(self):
        return self.map

