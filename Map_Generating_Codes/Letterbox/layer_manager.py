import os
import folium
import gpxpy
from map_utils import MapUtils
from font_manager import FontManager

class LayerManager:
    def __init__(self, map_object, base_places, base_colors, overlay_tree):
        self.map = map_object
        self.base_places = base_places
        self.base_colors = base_colors
        self.overlay_tree = overlay_tree
        self.regions = MapUtils.geocode_places(base_places)  # Initialize regions by geocoding places
        self.gpx_layers = []  # List to store GPX layers

    def add_layers(self):
        for i, (base_group, region) in enumerate(zip(self.base_places, self.regions)):
            # Get the base color for this region
            base_color = self.base_colors[i % len(self.base_colors)]

            # Create a bold and colored region label
            region_label = FontManager.get_subheader_font(f'Region {i+1}', color=base_color)
            region_children = []

            for j, (suburb_name, (index, row)) in enumerate(zip(base_group, region.iterrows())):
                suburb_short_name = suburb_name.split(',')[0]  # Extract only the suburb name
                suburb_layer = folium.FeatureGroup(name=suburb_short_name, show=False)

                # Adjust both hue and brightness for each suburb using MapUtils methods
                hue_factor = (j / max(len(base_group) - 1, 1)) * 0.2  # Small hue adjustment
                brightness_factor = 0.7 + (j / max(len(base_group) - 1, 1)) * 0.5
                shade = MapUtils.adjust_hue(base_color, hue_factor)
                shade = MapUtils.adjust_brightness(shade, brightness_factor)

                folium.GeoJson(
                    row['geometry'],
                    style_function=lambda x, color=shade: {'color': color},
                    name=suburb_short_name
                ).add_to(suburb_layer)

                suburb_layer.add_to(self.map)
                region_children.append({
                    "label": FontManager.get_label_font(f'{suburb_short_name}', color=shade),
                    "layer": suburb_layer,
                    "collapsed": True
                })

            # Add the region to the "Regions and Suburbs" section
            self.overlay_tree["children"][0]["children"].append({
                "label": region_label,
                "select_all_checkbox": True,
                "collapsed": True,
                "children": region_children
            })

    def add_gpx_route(self, gpx_file, layer_name="GPX Route", color='blue', show=True):
        with open(gpx_file, 'r') as f:
            gpx = gpxpy.parse(f)

        route_layer = folium.FeatureGroup(name=layer_name, show=show)  # `show=True` makes it visible by default

        for track in gpx.tracks:
            for segment in track.segments:
                points = [(point.latitude, point.longitude) for point in segment.points]
                folium.PolyLine(points, color=color, weight=2.5, opacity=1).add_to(route_layer)

        route_layer.add_to(self.map)
        
        # Add GPX route to the GPX layers list
        self.gpx_layers.append({
            "label": FontManager.get_label_font(layer_name), 
            "layer": route_layer,
            "collapsed": False
        })

    def add_gpx_routes(self, folder_path, color='black', show=True):
        for filename in os.listdir(folder_path):
            if filename.endswith(".gpx"):
                gpx_file_path = os.path.join(folder_path, filename)
                layer_name = filename.split(".gpx")[0]  # Use the file name (without extension) as the layer name
                self.add_gpx_route(gpx_file_path, layer_name, color, show)

    def get_gpx_layers(self):
        return self.gpx_layers
