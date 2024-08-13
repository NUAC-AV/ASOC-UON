import os
import folium
import gpxpy

class GPXHandler:
    def __init__(self, map_object):
        self.map = map_object
        self.gpx_layers = []

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
        self.gpx_layers.append({"label": layer_name, "layer": route_layer, "collapsed": False})

    def add_gpx_routes(self, folder_path, color='black'):
        for filename in os.listdir(folder_path):
            if filename.endswith(".gpx"):
                gpx_file_path = os.path.join(folder_path, filename)
                layer_name = filename.split(".gpx")[0]  # Use the file name (without extension) as the layer name
                self.add_gpx_route(gpx_file_path, layer_name, color)

    def get_gpx_layers(self):
        return self.gpx_layers
