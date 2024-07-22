import folium
import gpxpy

"""
Creates a function that creates a route map with markers.

Inputs:
- gpx_files: List of GPX route base layers (list of str)
- output_file: The name of the HTML map file (str)
- map_settings: Initializes the map settings
    - center: Node used to center map
    - zoom: Scale factor
- start_marker: Dictionary with start marker details
    - name: Name of marker
    - link: Google pin link
    - icon: Icon symbol used
    - colour: Colour of icon
    - description: Description given for marker
- end_marker: Dictionary with end marker details
    - name: Name of marker
    - icon: Icon symbol used
    - colour: Colour of icon
    - description: Description given for marker
"""

def create_map_with_markers(gpx_files, output_file, map_settings, start_markers, end_marker, route_styles):
    # Initialize a list to store all route coordinates
    all_routes = []

    # Process each GPX file
    for gpx_file in gpx_files:
        with open(gpx_file, 'r') as f:
            gpx = gpxpy.parse(f)

        # Extract coordinates from the GPX file
        route = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    route.append((point.latitude, point.longitude))
        
        # Add the extracted route to the list of all routes
        all_routes.append(route)

    # Unpack map settings
    centre, zoom = map_settings

    # Use the first route's starting point as the map's starting point
    if all_routes and all_routes[0]:
        start_point = all_routes[0][centre]
    else:
        start_point = [0, 0]

    # Initialize map layer
    m = folium.Map(location=start_point, zoom_start=zoom)

   # Add each GPX route to the map with the specified styles
    for route, style in zip(all_routes, route_styles):
        folium.PolyLine(
            route, 
            color=style.get('color', 'blue'), 
            weight=style.get('weight', 2.5), 
            opacity=style.get('opacity', 1)
        ).add_to(m)



    # Add start markers
    add_marker_to_map(m, all_routes[0][0], start_markers[0])

    add_marker_to_map(m, all_routes[1][0], start_markers[1])

    # Add end marker
    add_marker_to_map(m, all_routes[-1][-1], end_marker)

    # Save the map as an HTML file
    m.save(output_file)
    print(f"Map has been saved to {output_file}")


def add_marker_to_map(map_obj, location, marker_info):
    """
    Adds a marker to the given map object.

    Parameters:
    map_obj (folium.Map): The map object to add the marker to
    location (tuple): The latitude and longitude for the marker
    marker_info (dict): Dictionary containing marker information
    """
    name = marker_info.get("name", "")
    link = marker_info.get("link", "")
    icon = marker_info.get("icon", "info-sign")
    colour = marker_info.get("colour", "blue")
    description = marker_info.get("description", "")

    # Check if the icon is the ASOC logo and initialize the logo
    if icon == 'asoc':
        custom_icon_path = "Pictures/ASOC-Logo-orange.png"
        custom_icon = folium.CustomIcon(custom_icon_path, icon_size=(70, 32))
    else:
        custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')

    # Add marker to the map
    popup_content = f"<b>{name}</b><br>{description}"
    if link:
        popup_content = f"<b>{name}</b><br><a href='{link}' target='_blank'>Google Maps Link</a><br>{description}"

    folium.Marker(
        location=location,
        popup=popup_content,
        tooltip=name,
        icon=custom_icon
    ).add_to(map_obj)



# Example usage
gpx_files = [
    'GPX_Routes/Basden_Theatre/Science_Lane_Parking.gpx',
    'GPX_Routes/Basden_Theatre/Physics_Parking.gpx'
]
output_file = 'Church_Locations/Library_Church.html'
map_settings = (5, 35)  # Center index and zoom level
start_markers = [
    {
        "name": "Park her for service.",
        "link": "https://www.google.com/maps/place/Parking+lot,+Callaghan+NSW+2308/@-32.892825,151.6967984,19.24z/data=!4m6!3m5!1s0x6b733fd6ed40ea51:0xd0018d02fa4ab5b9!8m2!3d-32.8926406!4d151.6967744!16s%2Fg%2F11c1j793_h?entry=ttu",
        "icon": "square-parking",
        "colour": "darkpurple",
        "description": "Parking is limited here. So please reserve it for people with food, equipment or poor mobility."
    },
    {
        "name": "Please Park here",
        "link": "https://www.google.com/maps/place/Parking+lot,+Callaghan+NSW+2308/@-32.8930431,151.6966156,19.03z/data=!4m6!3m5!1s0x6b733fd69f626e5d:0xfd63acc8e85cad8d!8m2!3d-32.8936394!4d151.6962264!16s%2Fg%2F11c0vp7ggl?entry=ttu",
        "icon": "square-parking",
        "colour": "darkpurple",
        "description": "Follow route to church service."
    }
]

end_marker = {
    "name": "Church",
    "icon": "asoc",
    "colour": "red",
    "description": "Church"
}

route_styles = [
    {"color": "red", "weight": 3, "opacity": 0.8},
    {"color": "blue", "weight": 3, "opacity": 1}
]

create_map_with_markers(gpx_files, output_file, map_settings, start_markers, end_marker, route_styles)
