import folium
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
        self.colours = [
            'black', 'gray', 'blue', 'darkred', 'purple', 'red',
            'green', 'white', 'darkblue', 'darkpurple', 'cadetblue', 'orange',
            'pink', 'darkgreen'
        ]
        self.overlay_tree = {"label": "Regions and Suburbs", "select_all_checkbox": "Un/select all", "collapsed": True, "children": []}
        self.gpx_layers = []


    def _geocode_places(self):
        regions = []
        for base_group in self.base_places:
            places = [f"{place}, Newcastle, Australia" for place in base_group]
            region = ox.geocode_to_gdf(places)
            regions.append(region)
        return regions


    def _add_layers(self):
        for i, (base_group, region) in enumerate(zip(self.base_places, self.regions)):
            region_label = f"Region {i+1}"
            region_children = []

            for j, (suburb_name, (index, row)) in enumerate(zip(base_group, region.iterrows())):
                suburb_short_name = suburb_name.split(',')[0]  # Extract only the suburb name
                suburb_layer = folium.FeatureGroup(name=suburb_short_name, show=False)

                folium.GeoJson(
                    row['geometry'],
                    style_function=lambda x, color=self.colours[j % len(self.colours)]: {'color': color},
                    name=suburb_short_name
                ).add_to(suburb_layer)

                suburb_layer.add_to(self.map)
                region_children.append({"label": suburb_short_name, "layer": suburb_layer, "collapsed": True})

            self.overlay_tree["children"].append({"label": region_label, "select_all_checkbox": True, "collapsed": True, "children": region_children})
    

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


    def add_gpx_routes(self, folder_path, color='red'):
        for filename in os.listdir(folder_path):
            if filename.endswith(".gpx"):
                gpx_file_path = os.path.join(folder_path, filename)
                layer_name = filename.split(".gpx")[0]  # Use the file name (without extension) as the layer name
                self.add_gpx_route(gpx_file_path, layer_name, color)

    
    def add_tree_layer_control(self):
        self._add_layers()

        # Add GPX routes to the tree
        if self.gpx_layers:
            gpx_tree = {"label": "Compleated streets", "select_all_checkbox": True, "collapsed": True, "children": self.gpx_layers}
            self.overlay_tree["children"].append(gpx_tree)

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
