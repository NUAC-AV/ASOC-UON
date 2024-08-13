import colorsys
import matplotlib.colors as mcolors
import numpy as np
import folium
from folium import Element
import os
import osmnx as ox
import gpxpy
from folium.plugins import TreeLayerControl


class MapWithTreeLayerControl:
    def __init__(self, base_places, map_location=(-32.9, 151.79), zoom_start=12):
        self.base_places = base_places
        self.map_location = map_location
        self.zoom_start = zoom_start
        self.regions = self._geocode_places()
        self.map = folium.Map(location=self.map_location, zoom_start=self.zoom_start)
        self.base_colors = [
            '#1f77b4',  # blue
            '#ff7f0e',  # orange
            '#2ca02c',  # green
            '#d62728',  # red
            '#9467bd',  # purple
            '#8c564b',  # brown
            '#e377c2',  # pink
        ]
        self.gpx_layers = []

        # Initialize the overlay tree structure
        self.overlay_tree = {
            "label": "Maps",
            "select_all_checkbox": "Un/select all",
            "collapsed": False,
            "children": [
                {
                    "label": "<strong>Regions and Suburbs</strong>",
                    "select_all_checkbox": True,
                    "collapsed": True,
                    "children": []  # Will be populated in _add_layers
                },
                {
                    "label": "<strong>Completed Streets</strong>",
                    "select_all_checkbox": True,
                    "collapsed": False,
                    "children": self.gpx_layers  # Add GPX layers here
                }
            ]
        }

    def _adjust_brightness(self, color, factor):
        """ Adjusts brightness of a given color by the provided factor. """
        color = np.array(mcolors.to_rgb(color))
        adjusted_color = np.clip(color * factor, 0, 1)
        return mcolors.to_hex(adjusted_color)
    
    def _adjust_hue(self, color, hue_factor):
        """ Adjusts the hue of a given color to its complementary color. """
        color = np.array(mcolors.to_rgb(color))
        h, l, s = colorsys.rgb_to_hls(*color)
        new_h = (h + 0.5 * hue_factor) % 1.0
        adjusted_color = colorsys.hls_to_rgb(new_h, l, s)
        return mcolors.to_hex(adjusted_color)

    def _geocode_places(self):
        regions = []
        for base_group in self.base_places:
            places = [f"{place}, Newcastle, Australia" for place in base_group]
            region = ox.geocode_to_gdf(places)
            regions.append(region)
        return regions

    def _add_layers(self):
        for i, (base_group, region) in enumerate(zip(self.base_places, self.regions)):
            # Get the base color for this region
            base_color = self.base_colors[i % len(self.base_colors)]

            # Create a bold and colored region label
            region_label = f'<strong><span style="color: {base_color};">Region {i+1}</span></strong>'
            region_children = []

            for j, (suburb_name, (index, row)) in enumerate(zip(base_group, region.iterrows())):
                suburb_short_name = suburb_name.split(',')[0]  # Extract only the suburb name
                suburb_layer = folium.FeatureGroup(name=suburb_short_name, show=False)

                # Adjust both hue and brightness for each suburb
                hue_factor = (j / max(len(base_group) - 1, 1)) * 0.2  # Small hue adjustment
                brightness_factor = 0.7 + (j / max(len(base_group) - 1, 1)) * 0.5
                shade = self._adjust_hue(base_color, hue_factor)
                shade = self._adjust_brightness(shade, brightness_factor)

                folium.GeoJson(
                    row['geometry'],
                    style_function=lambda x, color=shade: {'color': color},
                    name=suburb_short_name
                ).add_to(suburb_layer)

                suburb_layer.add_to(self.map)
                region_children.append({
                    "label": f'<span style="color: {shade};">{suburb_short_name}</span>',
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

    def add_gpx_route(self, gpx_file, layer_name="GPX Route", color='blue'):
        with open(gpx_file, 'r') as f:
            gpx = gpxpy.parse(f)

        route_layer = folium.FeatureGroup(name=layer_name, show=False)

        for track in gpx.tracks:
            for segment in track.segments:
                points = [(point.latitude, point.longitude) for point in segment.points]
                folium.PolyLine(points, color=color, weight=2.5, opacity=1).add_to(route_layer)

        route_layer.add_to(self.map)
        
        # Add GPX route to the GPX layers list
        self.gpx_layers.append({"label": layer_name, "layer": route_layer, "collapsed": True})

    def add_gpx_routes(self, folder_path, color='black'):
        for filename in os.listdir(folder_path):
            if filename.endswith(".gpx"):
                gpx_file_path = os.path.join(folder_path, filename)
                layer_name = filename.split(".gpx")[0]  # Use the file name (without extension) as the layer name
                self.add_gpx_route(gpx_file_path, layer_name, color)

    def _add_custom_css(self):
        custom_css = """
        <style>
        /* Increase the size of the layer control */
        .leaflet-control-layers {
            font-size: 16px;  /* Increase font size */
            padding: 10px;    /* Add padding around the control */
            width: 300px;     /* Increase width of the control */
        }
        .leaflet-control-layers-toggle {
            width: 40px;  /* Adjust the toggle button width */
            height: 40px; /* Adjust the toggle button height */
            background-size: 40px 40px; /* Adjust background icon size */
            background-image: url('Images/ASOC-Logo-orange.png');  /* Use your custom image */
            background-repeat: no-repeat;
            background-position: center;
        }
        .leaflet-control-layers-overlays label {
            font-size: 16px;  /* Increase font size of labels */
            padding: 5px 10px;  /* Add padding to labels */
        }
        </style>
        """
        self.map.get_root().html.add_child(Element(custom_css))

    def add_tree_layer_control(self):
        self._add_layers()  # Populate the "Regions and Suburbs" section

        # Create the TreeLayerControl for both sections
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

        self._add_custom_css()

    def save_map(self, output_html):
        self.map.save(output_html)

    def display_map(self):
        return self.map

