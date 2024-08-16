import math
import re
from typing import List, Dict, Tuple, Any, Optional
from map_utils import MapUtils

class SuburbManager:
    def __init__(self, base_places: List[List[str]], location: str = "Newcastle, Australia") -> None:
        self.base_places: List[List[str]] = base_places
        self.location: str = location
        self.suburb_data: List[Dict[str, Any]] = self.initialize_suburbs()

    def initialize_suburbs(self) -> List[Dict[str, Any]]:
        """ Initialize the suburb data with names, feature groups, GeoJSON, centroids, zoom levels, and regions. """
        suburb_data = []
        geojson_data = MapUtils.geocode_places(self.base_places, self.location)  # Use MapUtils to geocode places

        for region_index, (base_group, geojson) in enumerate(zip(self.base_places, geojson_data)):
            region_name = f"Region {region_index + 1}"  # Assign region based on sublist index
            for suburb_name, (index, row) in zip(base_group, geojson.iterrows()):
                suburb_short_name = suburb_name.split(',')[0]  # Extract only the suburb name
                geometry = row['geometry']
                centroid = geometry.centroid  # Calculate the centroid of the GeoJSON
                zoom_level = self.calculate_zoom_level(geometry)  # Calculate the zoom level

                suburb_info = {
                    "name": suburb_short_name,
                    "geojson": geometry,
                    "centroid": (centroid.y, centroid.x),  # Store the centroid as (latitude, longitude)
                    "zoom_level": zoom_level,
                    "region": region_name,  # Add region information
                    "feature_group": None  # Placeholder for feature group, to be populated later
                }
                suburb_data.append(suburb_info)

        return suburb_data

    def calculate_zoom_level(self, geometry: Any, map_width_px: int = 800, map_height_px: int = 600, zoom_bias: float = 2.5) -> int:
        """
        Estimates an appropriate zoom level for the given geometry.

        :param geometry: The GeoJSON geometry to calculate the zoom level for.
        :param map_width_px: The width of the map display area in pixels.
        :param map_height_px: The height of the map display area in pixels.
        :param zoom_bias: A bias factor to adjust the zoom level. Increase this to zoom in more.
        :return: An estimated zoom level as an integer.
        """
        bounds = geometry.bounds  # Get the bounding box (min_lon, min_lat, max_lon, max_lat)
        min_lon, min_lat, max_lon, max_lat = bounds

        # Calculate the latitude and longitude differences
        lat_diff = max_lat - min_lat
        lon_diff = max_lon - min_lon

        # Convert latitude and longitude differences to meters using an approximate conversion
        lat_diff_m = lat_diff * 111_320  # Approximate meters per degree latitude
        lon_diff_m = lon_diff * 111_320 * math.cos(math.radians((min_lat + max_lat) / 2))  # Adjust for latitude

        # Calculate the maximum required zoom level based on the larger of the two dimensions
        max_dim_m = max(lat_diff_m, lon_diff_m)

        # Estimate zoom level based on map dimensions and max_dim_m
        # Formula: Z = log2(Earth circumference in meters / max_dim_m)
        # The Earth’s circumference at the equator is approximately 40,075,017 meters.
        # Here we assume a certain pixel resolution of the map, for example, 256px per tile at zoom level 0.
        zoom_level = math.log2(40_075_017 / max_dim_m) - math.log2(max(map_width_px, map_height_px) / 256)

        # Apply the zoom bias
        zoom_level += zoom_bias

        # Clamp the zoom level to reasonable limits (e.g., between 1 and 18)
        zoom_level = max(1, min(18, round(zoom_level)))

        return zoom_level

    def extract_suburb_data(self, html_content: str) -> None:
        """Extracts feature groups and assigns them to the corresponding suburbs."""
        # Simplified regex pattern to match and capture name and feature_group
        pattern = re.compile(r'''
            "label":\s*"\\u003cstrong\\u003e\\u003cspan\sstyle=\\"font-size:\s*[^;]+;\s*color:\s*[^;]+;\\"\\u003e(?P<name>[^\\]+)\\u003c/span\\u003e\\u003c/strong\\u003e",\s*
            "layer":\s*(?P<feature_group>feature_group_[^,]+),
        ''', re.VERBOSE)

        # Find all matches in the HTML content
        matches = pattern.findall(html_content)

        # Update the suburb_data with the extracted feature groups
        for name, feature_group in matches:
            for suburb in self.suburb_data:
                if suburb["name"] == name:
                    suburb["feature_group"] = feature_group

    def set_feature_group(self, suburb_name: str, feature_group: str) -> None:
        """Assigns a feature group to a specific suburb by name."""
        for suburb in self.suburb_data:
            if suburb["name"] == suburb_name:
                suburb["feature_group"] = feature_group

    def get_suburb_info(self) -> List[Dict[str, Any]]:
        """Returns the list of all suburb data."""
        return self.suburb_data

    def get_geojson_by_name(self, suburb_name: str) -> Optional[Any]:
        """Returns the GeoJSON data for a specific suburb by name."""
        for suburb in self.suburb_data:
            if suburb["name"] == suburb_name:
                return suburb["geojson"]
        return None

    def get_centroid_by_name(self, suburb_name: str) -> Optional[Tuple[float, float]]:
        """Returns the centroid (latitude, longitude) for a specific suburb by name."""
        for suburb in self.suburb_data:
            if suburb["name"] == suburb_name:
                return suburb["centroid"]
        return None

    def get_zoom_level_by_name(self, suburb_name: str) -> Optional[int]:
        """Returns the zoom level for a specific suburb by name."""
        for suburb in self.suburb_data:
            if suburb["name"] == suburb_name:
                return suburb["zoom_level"]
        return None

