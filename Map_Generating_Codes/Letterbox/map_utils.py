import numpy as np
import matplotlib.colors as mcolors
import colorsys
import osmnx as ox
from shapely.geometry import shape
import folium


class MapUtils:
    @staticmethod
    def adjust_brightness(color, factor):
        """ Adjusts brightness of a given color by the provided factor. """
        color = np.array(mcolors.to_rgb(color))
        adjusted_color = np.clip(color * factor, 0, 1)
        return mcolors.to_hex(adjusted_color)

    @staticmethod
    def adjust_hue(color, hue_factor):
        """ Adjusts the hue of a given color by the provided factor. """
        color = np.array(mcolors.to_rgb(color))
        h, l, s = colorsys.rgb_to_hls(*color)
        new_h = (h + 0.5 * hue_factor) % 1.0
        adjusted_color = colorsys.hls_to_rgb(new_h, l, s)
        return mcolors.to_hex(adjusted_color)

    @staticmethod
    def geocode_places(base_places, location="Newcastle, Australia"):
        """ Geocodes a list of places to their geographical coordinates. """
        regions = []
        for base_group in base_places:
            places = [f"{place}, {location}" for place in base_group]
            region = ox.geocode_to_gdf(places)
            regions.append(region)
        return regions
    
