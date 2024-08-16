import re
import osmnx as ox


class SuburbData:
    def __init__(self, names, feature_groups, geojson):
        self.name = names
        self.feature_group = feature_groups
        self.geojson = geojson