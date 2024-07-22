from Create_suburbs import MapWithTreeLayerControl

# Define base places
base_places = [
    ["Birmingham Gardens", "Shortland", "Jesmond", "North Lambton", "Waratah West", "Waratah", "Georgetown", "Hamilton North"],
    ["Carrington", "Islington", "Maryville", "Mayfield", "Mayfield East", "Mayfield West", "Tighes Hill", "Warabrook", "Wickham"],
    ["Broadmeadow", "Lambton", "New Lambton"],
    ["Elermore Vale"]
]

# Create the map with TreeLayerControl
map_control = MapWithTreeLayerControl(base_places)


# Add a GPX route
gpx_file = "GPX_Files/Misc/Afternoon_Run.gpx"  # Replace with your GPX file path
map_control.add_gpx_routes("GPX_Files/Misc")


map_control.add_tree_layer_control()

# Save the map to an HTML file
output_html = "Maps/Letterbox/letterbox_test_1.html"
map_control.save_map(output_html)

# Display the map in a Jupyter notebook (optional)
#map_with_tree.display_map()



#map_control = MapWithTreeLayerControl(base_places)
#map_control.add_gpx_route(gpx_file, layer_name="My GPX Route")
#map_control.add_tree_layer_control()
#map_control.save_map(output_html)
#map_control.display_map()