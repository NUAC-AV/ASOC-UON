from map_utils import MapUtils

class SuburbManager:
    def __init__(self, base_places, location="Newcastle, Australia"):
        self.base_places = base_places
        self.location = location
        self.suburb_data = self.initialize_suburbs()


    def initialize_suburbs(self):
        """ Initialize the suburb data with names, feature groups, and GeoJSON. """
        suburb_data = []
        geojson_data = MapUtils.geocode_places(self.base_places, self.location)  # Use MapUtils to geocode places

        for base_group, geojson in zip(self.base_places, geojson_data):
            for suburb_name, (index, row) in zip(base_group, geojson.iterrows()):
                suburb_short_name = suburb_name.split(',')[0]  # Extract only the suburb name
                suburb_info = {
                    "name": suburb_short_name,
                    "geojson": row['geometry'],
                    "feature_group": None  # Placeholder for feature group, to be populated later
                }
                suburb_data.append(suburb_info)

        return suburb_data
    

    def extract_suburb_data(self, html_content):
        """Extracts feature groups and assigns them to the corresponding suburbs."""
        # Simplified regex pattern to match and capture name and feature_group
        pattern = re.compile(r'''
            "label":\s*"\\u003cstrong\\u003e\\u003cspan\sstyle=\\"font-size:\s*[^;]+;\s*color:\s*[^;]+;\\"\\u003e(?P<name>[^\\]+)\\u003c/span\\u003e\\u003c/strong\\u003e",\s*
            "layer":\s*(?P<feature_group>feature_group_[^,]+),
        ''', re.VERBOSE)

        # Find all matches in the HTML content
        matches = pattern.findall(html_content)

        # Update the suburb_data with the extracted feature groups
        for match in matches:
            name, feature_group = match
            for suburb in self.suburb_data:
                if suburb["name"] == name:
                    suburb["feature_group"] = feature_group


    def set_feature_group(self, suburb_name, feature_group):
        """ Assigns a feature group to a specific suburb by name. """
        for suburb in self.suburb_data:
            if suburb["name"] == suburb_name:
                suburb["feature_group"] = feature_group


    def get_suburb_info(self):
        """ Returns the list of all suburb data. """
        return self.suburb_data


    def get_geojson_by_name(self, suburb_name):
        """ Returns the GeoJSON data for a specific suburb by name. """
        for suburb in self.suburb_data:
            if suburb["name"] == suburb_name:
                return suburb["geojson"]

        return None
