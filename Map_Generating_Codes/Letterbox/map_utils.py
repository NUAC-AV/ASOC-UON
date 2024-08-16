import os
import math
import colorsys
from typing import List, Any, Union, Dict, Tuple

import numpy as np
import matplotlib.colors as mcolors
import osmnx as ox
from shapely.geometry import shape
import folium
from folium import Element

from font_manager import FontManager

class MapUtils:
    EARTH_CIRCUMFERENCE_METERS = 40_075_017  # Earth's circumference at the equator in meters

    @staticmethod
    def adjust_brightness(color: Union[str, tuple], factor: float) -> str:
        """ Adjusts brightness of a given color by the provided factor. """
        color = np.array(mcolors.to_rgb(color))
        adjusted_color = np.clip(color * factor, 0, 1)
        return mcolors.to_hex(adjusted_color)


    @staticmethod
    def adjust_hue(color: Union[str, tuple], hue_factor: float) -> str:
        """ Adjusts the hue of a given color by the provided factor. """
        color = np.array(mcolors.to_rgb(color))
        h, l, s = colorsys.rgb_to_hls(*color)
        new_h = (h + 0.5 * hue_factor) % 1.0
        adjusted_color = colorsys.hls_to_rgb(new_h, l, s)
        return mcolors.to_hex(adjusted_color)


    @staticmethod
    def geocode_places(base_places: List[List[str]], location: str = "Newcastle, Australia") -> List[Any]:
        """ Geocodes a list of places to their geographical coordinates. """
        regions = []
        for base_group in base_places:
            places = [f"{place}, {location}" for place in base_group]
            region = ox.geocode_to_gdf(places)
            regions.append(region)
        return regions


    @staticmethod
    def add_css(map_object: folium.Map) -> None:
        custom_css = """
        <style>
        /* Increase the size of the layer control */
        .leaflet-control-layers {
            font-size: 16px;  /* Increase font size */
            padding: 5px;    /* Add padding around the control */
            width: 330px;     /* Increase width of the control */
            max-height: 280px; /* Reduce maximum height of the control */
            overflow-y: auto; /* Enable vertical scrolling */
        }
        .leaflet-control-layers-toggle {
            width: 45px;  /* Adjust the toggle button width */
            height: 45px; /* Adjust the toggle button height */
            background-size: 80px 80px; /* Adjust background icon size */
            background-image: url('Images/ASOC-Logo-orange.png');  /* Use your custom image */
            background-repeat: no-repeat;
            background-position: center;
        }
        .leaflet-control-layers-overlays label {
            font-size: 18px;  /* Increase font size of labels */
            padding: 5px 10px;  /* Add padding to labels */
        }
        /* Increase the size of checkboxes */
        input[type="checkbox"] {
            width: 20px;
            height: 20px;
            transform: scale(1.5); /* Adjust the scale factor as needed */
            transform-origin: top left;
            margin-right: 15px; /* Add space between the checkbox and text */
            margin-top: 4px;    /* Add a small margin above the checkbox */
            margin-bottom: 4px; /* Add a small margin below the checkbox */
        }
        </style>
        """
        
        map_object.get_root().html.add_child(Element(custom_css))


    @staticmethod
    def post_process_html(filename: Union[str, bytes, os.PathLike]) -> None:
        """Post-process the HTML file by removing the last five lines and adding the correct content."""
        # Read the HTML file into a string
        with open(filename, 'r') as file:
            html_as_string = file.read()

        # Split the HTML content into lines
        html_lines = html_as_string.splitlines()

        # Capture the fourth-to-last line which contains the addTo(map_...) statement
        map_add_line = html_lines[-4].strip() if len(html_lines) >= 4 else ""

        # Remove the last five lines
        if len(html_lines) >= 5:
            html_lines = html_lines[:-5]

        # Generate the replacement lines using the FontManager
        replacement_lines = [
            "{",
            f"    \"closedSymbol\": \"{FontManager.get_closed_symbol()}\",",
            f"    \"collapseAll\": \"{FontManager.get_collapse_all_label()}\",",
            f"    \"expandAll\": \"{FontManager.get_expand_all_label()}\",",
            f"    \"labelIsSelector\": \"both\",",
            f"    \"namedToggle\": false,",
            f"    \"openedSymbol\": \"{FontManager.get_opened_symbol()}\",",
            f"    \"selectorBack\": false,",
            f"    \"spaceSymbol\": \"&nbsp;\"",
            "}",
            map_add_line,  # Reinsert the captured map add line without extra spaces
            "</script>",
            "</html>"
        ]

        # Combine the remaining lines with the replacement lines
        updated_html_lines = html_lines + replacement_lines

        # Join the lines back into a single string
        updated_html_content = "\n".join(updated_html_lines)

        # Write the updated content back to the file
        with open(filename, 'w') as file:
            file.write(updated_html_content)

        print("Post-processing completed successfully.")


    @staticmethod
    def get_region_zoom(suburbs: List[Dict]) -> Tuple[float, float, int]:
        # Calculate the bounding box of the suburb centroids
            min_lat = min(suburb["centroid"][0] for suburb in suburbs)
            max_lat = max(suburb["centroid"][0] for suburb in suburbs)
            min_lon = min(suburb["centroid"][1] for suburb in suburbs)
            max_lon = max(suburb["centroid"][1] for suburb in suburbs)

            # Calculate the centroid of the bounding box
            region_centroid = ((min_lat + max_lat) / 2, (min_lon + max_lon) / 2)

            # Estimate the zoom level based on the bounding box
            lat_diff = max_lat - min_lat
            lon_diff = max_lon - min_lon
            max_dim_m = max(lat_diff * 111_320, lon_diff * 111_320 * math.cos(math.radians(region_centroid[0])))

            # Calculate the zoom level for the region
            region_zoom_level = math.log2(40_075_017 / max_dim_m) - math.log2(max(800, 600) / 256)
            region_zoom_level = max(1, min(18, round(region_zoom_level)))

            # Apply the zoom bias
            region_zoom_level += 2

            return region_centroid, region_zoom_level
    

    @staticmethod
    def group_suburbs_by_region(suburb_data: List[Dict], js_code: str) -> Tuple[str, Dict]:
        """
        Groups suburbs by their region and appends JavaScript code for recentering the map on each suburb.

        :param suburb_data: A list of suburb data dictionaries containing names, feature groups, centroids, zoom levels, and regions.
        :param js_code: The existing JavaScript code string to which new code will be appended.
        :return: A tuple with the updated JavaScript code and a dictionary of grouped suburbs by region.
        """
        regions = {}

        for suburb in suburb_data:
            # Ensure each dictionary has the expected keys
            if all(key in suburb for key in ("feature_group", "centroid", "zoom_level", "name", "region")):
                suburb_name = suburb["name"]
                feature_group_var = suburb["feature_group"]
                latitude, longitude = suburb["centroid"]
                zoom_level = suburb["zoom_level"]
                region_name = suburb["region"]

                # Append the recenter block for each suburb to the existing js_code
                js_code += f"""
                // Recenter for {suburb_name}
                if (e.layer === {feature_group_var}) {{
                    console.log("Recenter to {suburb_name}");  // Debug: Log if condition is met
                    map.setView([{latitude:.5f}, {longitude:.5f}], {zoom_level}, {{
                        animate: true,
                        pan: {{duration: 1}}
                    }});
                }}
                """

                # Group suburbs by region
                if region_name not in regions:
                    regions[region_name] = []
                regions[region_name].append(suburb)

        return js_code, regions


    @staticmethod
    def generate_recenter_code(suburb_data: List[Dict], map_memory_number: str) -> str:
        """
        Generates the JavaScript code block to recenter the map on specific suburbs and regions when their layers are added.

        :param suburb_data: A list of suburb data dictionaries containing names, feature groups, centroids, zoom levels, and regions.
        :param map_memory_number: The unique identifier for the map (e.g., map_96432543117ac5c1a2617564a0927e1b).
        :return: A string containing the JavaScript code block.
        """
        # Initialize the JavaScript code
        js_code = f"""
        document.addEventListener('DOMContentLoaded', function() {{
            var map = {map_memory_number};  // Access the Leaflet map instance by its ID

            // Event listener for overlay addition
            map.on('overlayadd', function(e) {{
                console.log("Overlay added: ", e.layer);  // Debug: Log the layer added
        """

        # Updates regions and js_code.
        js_code, regions = MapUtils.group_suburbs_by_region(suburb_data, js_code)

        # Generate the recenter block for each region
        for region_name, suburbs in regions.items():
            region_centroid, region_zoom_level = MapUtils.get_region_zoom(suburbs)
            feature_groups = " && ".join([f"map.hasLayer({suburb['feature_group']})" for suburb in suburbs])

            js_code += f"""
            // Recenter for {region_name}
            if ({feature_groups}) {{
                console.log("Recenter to {region_name}");  // Debug: Log if condition is met
                map.setView([{region_centroid[0]:.5f}, {region_centroid[1]:.5f}], {region_zoom_level}, {{
                    animate: true,
                    pan: {{duration: 1}}
                }});
            }}
            """

        # Close the JavaScript block
        js_code += """
            });
        });
        """

        return js_code


    @staticmethod
    def insert_recenter_code_in_html(html_file_path: Union[str, bytes, os.PathLike], recenter_code: str) -> None:
        """
        Inserts the recentering JavaScript code into the second-to-last line of the HTML file.

        :param html_file_path: Path to the HTML file where the recenter code will be inserted.
        :param recenter_code: The JavaScript code to be inserted.
        """
        # Read the contents of the HTML file
        with open(html_file_path, 'r') as file:
            html_content = file.readlines()

        # Insert the recenter_code before the second last line
        if len(html_content) > 1:
            html_content.insert(-2, recenter_code + "\n")
        else:
            raise ValueError("The HTML file content is too short to insert recenter code")

        # Write the updated content back to the HTML file
        with open(html_file_path, 'w') as file:
            file.writelines(html_content)

        print(f"Recenter code successfully inserted into {html_file_path}.")
