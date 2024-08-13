from Create_suburbs import MapWithTreeLayerControl

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
gpx_file = "GPX_Files/Misc/Afternoon_Run.gpx"  # Replace with your GPX file path
map_control.add_gpx_routes("GPX_Files/Misc")


map_control.add_tree_layer_control()


# Save the map to an HTML file
output_html = f"Maps/Letterbox/letterbox_test_2.html"
map_control.save_map(output_html)

