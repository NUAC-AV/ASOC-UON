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
    def add_recenter_js_to_html(filename, suburb_data):
        """
        Adds JavaScript to recenter the map when specific suburb layers are selected.

        :param filename: Path to the HTML file to which the JS will be added.
        :param suburb_data: List of tuples with (suburb_name, feature_group_variable_name, coordinates).
        """
        # Read the HTML file content
        with open(filename, 'r') as file:
            html_as_string = file.read()

        # Get the map ID generated by Folium (usually it is 'map' but may vary)
        map_id = "map_" + html_as_string.split('id="map_', 1)[1].split('"', 1)[0]

        # Prepare the JavaScript to recenter the map on layer selection
        recenter_js = f"""
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var map = {map_id};  // Access the Leaflet map instance by its ID
        """

        # Generate the JavaScript for each suburb to recenter the map when its layer is selected
        recenter_js += """
            map.on('overlayadd', function(e) {
        """

        for suburb_name, feature_group_var, coordinates in suburb_data:
            recenter_js += f"""
                if (e.layer === {feature_group_var}) {{
                    map.setView([{coordinates[0]}, {coordinates[1]}], 13, {{
                        animate: true,
                        pan: {{duration: 1}}
                    }});
                }}
            """

        # Close the script tags
        recenter_js += """
            });
        });
        </script>
        """

        # Insert the JavaScript code before the closing </body> tag
        insertion_index = html_as_string.rfind('</body>')
        updated_html = html_as_string[:insertion_index] + recenter_js + html_as_string[insertion_index:]

        # Write the updated HTML back to the file
        with open(filename, 'w') as file:
            file.write(updated_html)

        print("Recenter JavaScript added successfully.")
