import gpxpy

# Function opens gpx files
def parse_gpx_files(gpx_files):
    all_routes = []
    for gpx_file in gpx_files:
        with open(gpx_file, 'r') as f:
            gpx = gpxpy.parse(f)
            route = [(point.latitude, point.longitude) for track in gpx.tracks for segment in track.segments for point in segment.points]
            all_routes.append(route)
    return all_routes