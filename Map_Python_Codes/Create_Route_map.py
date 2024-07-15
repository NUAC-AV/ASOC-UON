import folium
import gpxpy

def create_map_with_markers(gpx_file, output_file, map_settings, start_marker):
    """
    Creates a map with the given GPX route and a starting marker.

    Parameters:
    gpx_file (str): Path to the GPX file.
    output_file (str): Name of the output HTML file.
    map_settings (tuple): Center index and zoom level for the map.
    start_marker (dict): Dictionary containing start marker details. 
                         Example: {"name": "Library", "link": "www.something.com", "icon": "fire", "colour": "red", "description": "Starting point"}

    Returns:
    None
    """
    name = start_marker.get("name", "Start")
    link = start_marker.get("link", "#")
    icon = start_marker.get("icon", "info-sign")
    colour = start_marker.get("colour", "blue")
    description = start_marker.get("description", "Starting point")

    centre, zoom = map_settings

    # Parse the GPX file
    with open(gpx_file, 'r') as f:
        gpx = gpxpy.parse(f)

    # Extract coordinates from the GPX file
    route = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                route.append((point.latitude, point.longitude))

    # Create a map centered around the specified point
    if route:
        start_point = route[centre]
    else:
        start_point = [0, 0]

    # Initialize map layer
    m = folium.Map(location=start_point, zoom_start=zoom)
    
    # Add the GPX route to the map
    folium.PolyLine(route, color='blue', weight=2.5, opacity=1).add_to(m)

    # Make marker Icon
    custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')

    # Add start marker to the map
    folium.Marker(
        location=route[0],
        popup=f"<b>{name}</b><br><a href='{link}' target='_blank'>Google Maps Link</a><br>{description}",
        tooltip=name,
        icon=custom_icon
    ).add_to(m)

    # Save the map as an HTML file
    m.save(output_file)
    print(f"Map has been saved to {output_file}")

# Example usage
gpx_file = 'GPX_Routes/ASOC Library_Basden Theatre (BA) Church.gpx'
output_file = 'Church_Locations/Library_Church.html'
map_settings = (0, 15)  # Center index and zoom level
start_marker = {
    "name": "Library",
    "link": "www.something.com",
    "icon": "fire",
    "colour": "red",
    "description": "Starting point"
}

create_map_with_markers(gpx_file, output_file, map_settings, start_marker)
