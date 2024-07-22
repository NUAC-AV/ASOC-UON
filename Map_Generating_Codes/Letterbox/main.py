from Create_suburbs import MapWithTreeLayerControl

# Define base places
base_places = [
    ["Birmingham Gardens", "Shortland", "Jesmond", "North Lambton", "Waratah West", "Waratah", "Georgetown", "Hamilton North"],
    ["Carrington", "Islington", "Maryville", "Mayfield", "Mayfield East", "Mayfield West", "Tighes Hill", "Warabrook", "Wickham"],
    ["Broadmeadow", "Lambton", "New Lambton"],
    ["Elermore Vale"]
]

# Create the map with TreeLayerControl
map_with_tree = MapWithTreeLayerControl(base_places)
map_with_tree.add_tree_layer_control()

# Add a GPX route
gpx_file = "path/to/your/gpxfile.gpx"  # Replace with your GPX file path
#map_with_tree.add_gpx_route(gpx_file, layer_name="My GPX Route", color='blue')

# Save the map to an HTML file
output_html = "nested_sublayers_map_with_gpx.html"
map_with_tree.save_map(output_html)

# Display the map in a Jupyter notebook (optional)
map_with_tree.display_map()