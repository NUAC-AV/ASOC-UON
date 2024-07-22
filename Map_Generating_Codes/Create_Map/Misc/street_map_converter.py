import osmnx as ox
import pandas as pd
import geopandas as gpd
import os

class StreetMapConverter:
    def __init__(self, places):
        self.places = places
        self.graphs = []
        self.edges_gdfs = []

    def get_graphs(self):
        """Get street networks for each place."""
        self.graphs = [ox.graph_from_place(place, network_type='walk') for place in self.places]
        for i, graph in enumerate(self.graphs):
            print(f"Graph {i}:")
            print(graph)

    def convert_to_gdfs(self):
        """Convert graphs to GeoDataFrames."""
        for graph in self.graphs:
            _, edges = ox.graph_to_gdfs(graph)
            self.edges_gdfs.append(edges)

    def merge_gdfs(self):
        """Merge the GeoDataFrames."""
        self.merged_edges_gdf = gpd.GeoDataFrame(pd.concat(self.edges_gdfs, ignore_index=True))

    def save_to_geojson(self, output_directory, filename):
        """Save the merged GeoDataFrame to a GeoJSON file."""
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        output_path = os.path.join(output_directory, filename)
        self.merged_edges_gdf.to_file(output_path, driver='GeoJSON')
        print(f"GeoJSON saved to {output_path}")

    def process(self, output_directory="Letterbox_Maps/GeoJSON", filename="MAP1.geojson"):
        """Execute all steps."""
        self.get_graphs()
        self.convert_to_gdfs()
        self.merge_gdfs()
        self.save_to_geojson(output_directory, filename)
