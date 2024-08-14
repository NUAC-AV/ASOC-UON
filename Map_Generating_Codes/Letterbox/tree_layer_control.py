import folium
from folium import Element
from folium.plugins import TreeLayerControl
from custom_css import CustomCSS  
from layer_manager import LayerManager  
from map_utils import MapUtils  
from gpx_handler import GPXHandler  
from font_manager import FontManager 

class MapWithTreeLayerControl:
    def __init__(self, base_places, map_location=(-32.9, 151.79), zoom_start=12):
        self.base_places = base_places
        self.map_location = map_location
        self.zoom_start = zoom_start
        self.map = folium.Map(location=self.map_location, zoom_start=self.zoom_start)
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

        # Initialize LayerManager to handle layer creation
        self.layer_manager = LayerManager(self.map, self.base_places, self.base_colors, self.overlay_tree)
        self.layer_manager.add_layers()  # Add layers to the map

    def add_tree_layer_control(self):
        # Replace "Maps" label with the ASOC logo image
        self.overlay_tree["label"] = '<img src="../../Images/ASOC-Logo-orange.png" alt="ASOC Logo" style="width: 177px; height: 82px; vertical-align: middle;">'

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

        # Apply custom CSS from the separate class
        # css = CustomCSS(self.map)
        # css.add_css()
        # css.remove_end_lines()
        # #css.ammend_end_css()


    def save_map(self, output_html):
        self.map.save(output_html)

