def create_map(gpx, name):
    m = folium.Map(location=map_center, zoom_start=14)

    # Read the GPX file
    with open(gpx, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Extract route coordinates
    for track in gpx.tracks:
        for segment in track.segments:
            coords = [(point.latitude, point.longitude) for point in segment.points]
            folium.PolyLine(coords, color="blue", weight=2.5, opacity=1).add_to(m)

    # Add markers for the start and end points of the route
    if coords:
        folium.Marker(coords[0], popup="Start", icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(coords[-1], popup="End", icon=folium.Icon(color='red')).add_to(m)

    # Save the map as an HTML file
    m.save(name)