import numpy as np
import matplotlib.colors as mcolors
import colorsys
import osmnx as ox
from shapely.geometry import shape
import folium
from folium import Element

from font_manager import FontManager 

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


    @staticmethod
    def add_css(map_object):
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
    def post_process_html(filename):
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
    def generate_recenter_code(suburb_data, map_memory_number):
        """
        Generates the JavaScript code block to recenter the map on specific suburbs and regions
        when their layers are added.

        :param suburb_data: A list of suburb data dictionaries containing names, feature groups, centroids, zoom levels, and regions.
        :param map_memory_number: The unique identifier for the map (e.g., map_96432543117ac5c1a2617564a0927e1b).
        :return: A string containing the JavaScript code block.
        """
        # Ensure suburb_data is a list of dictionaries
        if not isinstance(suburb_data, list) or not all(isinstance(suburb, dict) for suburb in suburb_data):
            raise ValueError("suburb_data must be a list of dictionaries")

        js_code = f"""
        document.addEventListener('DOMContentLoaded', function() {{
            var map = {map_memory_number};  // Access the Leaflet map instance by its ID

            // Event listener for overlay addition
            map.on('overlayadd', function(e) {{
                console.log("Overlay added: ", e.layer);  // Debug: Log the layer added
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

                # Generate the recenter block for each suburb
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
                regions[region_name].append({
                    "feature_group": feature_group_var,
                    "centroid": (latitude, longitude),
                    "zoom_level": zoom_level
                })

        # Generate the recenter block for each region
        for region_name, suburbs in regions.items():
            region_centroid = np.mean([suburb["centroid"] for suburb in suburbs], axis=0)
            region_zoom_level = max(suburb["zoom_level"] for suburb in suburbs)
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
    def insert_recenter_code_in_html(html_file_path, recenter_code):
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
