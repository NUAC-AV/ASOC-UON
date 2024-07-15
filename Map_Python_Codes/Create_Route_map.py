import folium
import gpxpy

"""
Creates function that creates route map.
Taking the following inputs.
- gpx_file: The route baselayer. (Str)
- output_file: The name of the html map file. (Str)
- map_settings: Initalises the map settings 
    - center: Node used to center map.
    - zoom: Scale factor.
- start_marker: 
    - name: Name of marker
    - link: Google pin link
    - Icon: Icon symbol used
    - colour: Colour of icon
    - description: Description given for marker
- end_marker:
    - name: Name of marker
    - Icon: Icon symbol used
    - colour: Colour of icon
    - description: Description given for marker


"""
def create_map_with_markers(gpx_file, output_file, map_settings, start_marker, end_marker):
    # Open the GPX file
    with open(gpx_file, 'r') as f:
        gpx = gpxpy.parse(f)

    # Extract coordinates from the GPX file
    route = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                route.append((point.latitude, point.longitude))


    centre, zoom = map_settings
    # Create a map centered around the specified point
    if route:
        start_point = route[centre]
    else:
        start_point = [0, 0]

    # Initialize map layer
    m = folium.Map(location=start_point, zoom_start=zoom)
    
    # Add the GPX route to the map
    folium.PolyLine(route, color='blue', weight=2.5, opacity=1).add_to(m)


    # Get details for start_marker
    name = start_marker["name"]
    link = start_marker["link"]
    icon = start_marker["icon"]
    colour = start_marker["colour"]
    description = start_marker["description"]

    # Check if the icon is the ASOC logo and inalize the logo
    if icon == 'asoc':
        custom_icon = folium.CustomIcon(custom_icon_path, icon_size=(70, 32))
    else:
        custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')


    # Add start marker to the map
    folium.Marker(
        location=route[0],
        popup=f"<b>{name}</b><br><a href='{link}' target='_blank'>Google Maps Link</a><br>{description}",
        tooltip=name,
        icon=custom_icon
    ).add_to(m)


    # Get details for end_marker
    name = end_marker["name"]
    icon = end_marker["icon"]
    colour = end_marker["colour"]
    description = end_marker["description"]


    # Make endpoint marker Icon
    # Check if the icon is the ASOC logo and inalize the logo
    if icon == 'asoc':
        custom_icon_path = "Pictures/ASOC-Logo-orange.png"
        custom_icon = folium.CustomIcon(custom_icon_path, icon_size=(70,32))
    else:
        custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')

    # Add endpoint marker to the map
    folium.Marker(
        location=route[-1],
        popup=f"<b>{name}</b><br>{description}",
        tooltip=name,
        icon=custom_icon
    ).add_to(m)

   
    # Save the map as an HTML file
    m.save(output_file)
    print(f"Map has been saved to {output_file}")




# Example usage
gpx_file = 'GPX_Routes/ASOC Library_Basden Theatre (BA) Church.gpx'
output_file = 'Church_Locations/Library_Church.html'
map_settings = (5, 35)  # Center index and zoom level
start_marker = {
    "name": "Please Park here",
    "link": "https://www.google.com/maps/place/Parking+lot,+Callaghan+NSW+2308/@-32.8930431,151.6966156,19.03z/data=!4m6!3m5!1s0x6b733fd69f626e5d:0xfd63acc8e85cad8d!8m2!3d-32.8936394!4d151.6962264!16s%2Fg%2F11c0vp7ggl?entry=ttu",
    "icon": "square-parking",
    "colour": "darkpurple",
    "description": "Follow route to church service."
}
end_marker = {
    "name": "Church",
    "icon": "asoc",
    "colour": "red",
    "description": "Church"
}


create_map_with_markers(gpx_file, output_file, map_settings, start_marker, end_marker)
