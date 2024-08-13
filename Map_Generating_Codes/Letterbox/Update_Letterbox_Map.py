from Create_suburbs import MapWithTreeLayerControl
from gpx_handler import GPXHandler  # Import the GPXHandler class

# Define base places
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

# Create the map with TreeLayerControl
map_control = MapWithTreeLayerControl(base_places)


# Add a GPX route
#gpx_file = "GPX_Files/Misc/Afternoon_Run.gpx"  # Replace with your GPX file path
#map_control.add_gpx_routes("GPX_Files/Misc")
# Create an instance of GPXHandler and load the GPX routes
gpx_handler = GPXHandler(map_control.map)
gpx_handler.add_gpx_routes("GPX_Files/Misc")


map_control.overlay_tree["children"].append({
    "label": "Completed streets",
    "select_all_checkbox": True,
    "collapsed": False,
    "children": gpx_handler.get_gpx_layers()
})

# Add the tree layer control to the map
map_control.add_tree_layer_control()


# Save the map to an HTML file
output_html = f"Maps/Letterbox/letterbox_test_3.html"
map_control.save_map(output_html)
