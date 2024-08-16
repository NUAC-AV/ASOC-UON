import re
import folium
from folium.plugins import TreeLayerControl
from layer_manager import LayerManager  
from map_utils import MapUtils  
from font_manager import FontManager 
from suburb_manager import SuburbManager

class CreateMap:
    def __init__(self, base_places, gpx_folder, map_location=(-32.9, 151.79), zoom_start=12):
        self.base_places = base_places
        self.gpx_folder = gpx_folder
        self.map_location = map_location
        self.zoom_start = zoom_start
        self.map = folium.Map(location=self.map_location, zoom_start=self.zoom_start, zoom_control=False)
        self.map_memory_number = None
        self.base_colors = [
            '#1f77b4',  # blue
            '#ff7f0e',  # orange
            '#2ca02c',  # green
            '#d62728',  # red
            '#9467bd',  # purple
            '#8c564b',  # brown
            '#e377c2',  # pink
        ]

        # Initialize the overlay tree structure
        self.overlay_tree = {
            "label": "Maps",
            "select_all_checkbox": "Un/select all",
            "collapsed": False,
            "children": [
                {
                    "label": FontManager.get_header_font('Regions and Suburbs'),
                    "select_all_checkbox": True,
                    "collapsed": True,
                    "children": []  # Will be populated by LayerManager
                },
            ]
        }

        # Initialize LayerManager to handle both suburb and GPX layer creation
        self.layer_manager = LayerManager(self.map, self.base_places, self.base_colors, self.overlay_tree)
        self.layer_manager.add_layers()  # Add suburb layers to the map
        self.layer_manager.add_gpx_routes(self.gpx_folder)  # Add GPX layers to the map
        # Initialize the SuburbManager and store it as an attribute
        self.suburb_manager = SuburbManager(self.base_places)

    
    @staticmethod
    def get_map_memory_number(html_content):
        """
        Extracts the map memory number (map ID) from the given HTML content.

        :param html_content: The HTML content of the Folium map as a string.
        :return: The map memory number as a string.
        """
        # Regex pattern to find the map ID
        pattern = re.compile(r'id="map_([a-f0-9]+)"')
        match = pattern.search(html_content)

        if match:
            return f"map_{match.group(1)}"
        else:
            raise ValueError("Map memory number not found in the HTML content.")


    def apply_custom_css(self):
        # Apply custom CSS using MapUtils
        MapUtils.add_css(self.map)

    def add_tree_layer_control(self):
        # Replace "Maps" label with the ASOC logo image
        self.overlay_tree["label"] = '<img src="../../Images/ASOC-Logo-orange.png" alt="ASOC Logo" style="width: 205px; height: 90px; vertical-align: middle;">'

        # Create the TreeLayerControl for the sections
        tree_control = TreeLayerControl(
            base_tree=None,
            overlay_tree=self.overlay_tree,
            closed_symbol=FontManager.get_closed_symbol(symbol='&#x25A1;', color='blue'),
            opened_symbol=FontManager.get_opened_symbol(symbol='&#x25A0;', color='green'),
            space_symbol='&nbsp;',
            selector_back=False,
            named_toggle=False,
            collapse_all=FontManager.get_collapse_all_label(color='blue'),
            expand_all=FontManager.get_expand_all_label(color='green'),
            label_is_selector='both'
        )
        tree_control.add_to(self.map)


    def setup_map(self):
        self.apply_custom_css()
        self.add_tree_layer_control()

    # def save_map(self, output_html):
    #     self.map.save(output_html)
    #     # Post-process the HTML file to inject additional custom JavaScript or CSS, if needed
    #     MapUtils.post_process_html(output_html)
    #     # If needed, generate the suburb data for recentering and add recenter JS to the HTML file
    #     # suburb_data = MapUtils.generate_suburb_data(self.map, self.base_places)
    #     # MapUtils.add_recenter_js_to_html(output_html, suburb_data)

    #     # Generate and insert the recentering JavaScript
    #     #MapUtils.generate_recenter_code(output_html, self.map_memory_number)
    #     # In your CreateMap class, before calling generate_recenter_code:
    #     # print("Suburb Data:", self.suburb_manager.get_suburb_info())
    #     # print("Suburb Data Type:", type(self.suburb_manager.get_suburb_info()))

    #     # Generate and insert the recentering JavaScript
    #     self.suburb_manager.extract_suburb_data(html_content)
    #     self.generate_recenter_js(output_html)

    
    def initialize_map(self, output_html):
        """
        Initialize and save the map to an HTML file.
        """
        self.map.save(output_html)
        print(f"Map initialized and saved to {output_html} successfully.")


    def save_map(self, output_html):
        """
        Modify the saved HTML file to inject additional JavaScript and CSS.
        """
        # First, initialize and save the map
        self.initialize_map(output_html)
        
        # Post-process the HTML file to inject additional custom JavaScript or CSS, if needed
        MapUtils.post_process_html(output_html)
        
        # Read the saved HTML file to extract the feature groups
        with open(output_html, 'r') as file:
            html_content = file.read()

        # Extract feature groups using the SuburbManager
        self.suburb_manager.extract_suburb_data(html_content)

        # Get the map memory number (ID) from the map object
        map_memory_number = self.map.get_name()

        # Generate the recentering JavaScript code
        suburb_data = self.suburb_manager.get_suburb_info()
        recenter_code = MapUtils.generate_recenter_code(suburb_data, map_memory_number)

        # Insert the recentering JavaScript code into the HTML file
        MapUtils.insert_recenter_code_in_html(output_html, recenter_code)

        print(f"Modifications applied to {output_html} successfully.")
    
        #print(suburb_data)

            

