from folium import Element
from font_manager import FontManager

class CustomCSS:
    def __init__(self, map_object):
        self.map = map_object

    def add_css(self):
        custom_css = """
        <style>
        /* Increase the size of the layer control */
        .leaflet-control-layers {
            font-size: 16px;  /* Increase font size */
            padding: 10px;    /* Add padding around the control */
            width: 350px;     /* Increase width of the control */
        }
        .leaflet-control-layers-toggle {
            width: 50px;  /* Adjust the toggle button width */
            height: 50px; /* Adjust the toggle button height */
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
            transform: scale(1.5); /* Adjust the scale factor as needed */
            transform-origin: top left;
            margin-right: 15px; /* Add space between the checkbox and text */
            margin-top: 4px;    /* Add a small margin above the checkbox */
            margin-bottom: 4px; /* Add a small margin below the checkbox */
            /* Increase the font size of the open and closed symbols */
        }
        </style>
        """
        
        self.map.get_root().html.add_child(Element(custom_css))

    def remove_end_lines(self):
        """Remove the last five lines of the HTML content and update the map."""
        html_obj = self.map.get_root().html

        # Extract the HTML content as a string
        html_content = str(html_obj.render())

        # Split the HTML content into lines
        html_lines = html_content.splitlines()

        # Remove the last five lines
        html_lines = html_lines[:-5]

        # Join the remaining lines back into a single string
        updated_html_content = "\n".join(html_lines)

        # Replace the HTML content in the map object
        html_obj._children.clear()
        html_obj.add_child(Element(updated_html_content))


    def post_process_html(self, filename):
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

        # # Generate the replacement lines using the FontManager
        replacement_lines = [
            "{",
            f"    \"closedSymbol\": \"{FontManager.get_closed_symbol(symbol='&#x25A1;', color='blue')}\",",
            f"    \"collapseAll\": \"{FontManager.get_collapse_all_label(color='blue')}\",",
            f"    \"expandAll\": \"{FontManager.get_expand_all_label(color='green')}\",",
            f"    \"labelIsSelector\": \"both\",",
            f"    \"namedToggle\": false,",
            f"    \"openedSymbol\": \"{FontManager.get_opened_symbol(symbol='&#x25A0;', color='green')}\",",
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

       