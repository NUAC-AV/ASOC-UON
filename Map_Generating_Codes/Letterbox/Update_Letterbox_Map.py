from tree_layer_control import MapWithTreeLayerControl
from gpx_handler import GPXHandler  
from font_manager import FontManager
from custom_css import CustomCSS 

class UpdateLetterboxMap:
    def __init__(self, base_places, gpx_folder, output_html):
        self.base_places = base_places
        self.gpx_folder = gpx_folder
        self.output_html = output_html
        self.map_control = None
        self.gpx_handler = None

    def create_map(self):
        # Create the map with TreeLayerControl
        self.map_control = MapWithTreeLayerControl(self.base_places)

    def add_gpx_routes(self):
        # Create an instance of GPXHandler and load the GPX routes
        self.gpx_handler = GPXHandler(self.map_control.map)
        self.gpx_handler.add_gpx_routes(self.gpx_folder)

    def integrate_gpx_layers(self):
        # Integrate the GPX layers into the MapWithTreeLayerControl
        self.map_control.overlay_tree["children"].append({
            "label": FontManager.get_header_font('Completed Streets'),
            "select_all_checkbox": True,
            "collapsed": True,
            "children": self.gpx_handler.get_gpx_layers()
        })

    def add_tree_layer_control(self):
        # Add the tree layer control to the map
        self.map_control.add_tree_layer_control()

    def save_map(self):
        # Save the map to an HTML file
        self.map_control.save_map(self.output_html)

    def apply_custom_css(self):
        # Create an instance of CustomCSS and apply post-processing
        css = CustomCSS(self.map_control.map)
        css.post_process_html(self.output_html)

    def run(self):
        self.create_map()
        self.add_gpx_routes()
        self.integrate_gpx_layers()
        self.add_tree_layer_control()
        self.save_map()
        self.apply_custom_css()

if __name__ == "__main__":
    base_places = [
        ["Birmingham Gardens", "Shortland", "Jesmond", "North Lambton", "Waratah West", "Waratah", "Georgetown", "Hamilton North"],
        ["Carrington", "Islington", "Maryville", "Mayfield", "Mayfield East", "Mayfield West", "Tighes Hill", "Warabrook", "Wickham"],
        ["Broadmeadow", "Lambton", "New Lambton"],
        ["Elermore Vale", "Wallsend", "Maryland", "Fletcher", "Minmi"],
        ["Barnsley", "Cameron Park", "Edgeworth", "Killingworth", "West Wallsend", "Holmesville"],
        ["Argenton",  "Cardiff Heights", "Glendale", "New Lambton Heights", "Rankin Park"],
        ["Adamstown", "Adamstown Heights", "Garden Suburb", "Kotara", "Kotara South"],
        # ["Bar Beach", "Hamilton", "Hamilton South", "Merewether", "Merewether Heights", "The Junction"],
        # ["Cooks Hill", "Newcastle", "Newcastle East", "Newcastle West", "The Hill"],
        # ["Stockton", "Fern Bay"],
        # ["Boolaroo", "Cardiff", "Hillsborough", "Lakelands", "Macquarie Hills", "Speers Point"],
        # ["Charlestown", "Dudley", "Kahibah", "Highlands", "Whitebridge"]
    ]
    gpx_folder = "GPX_Files/Misc"
    output_html = "Maps/Letterbox/letterbox_test_12.html"
    
    app = UpdateLetterboxMap(base_places, gpx_folder, output_html)
    app.run()
