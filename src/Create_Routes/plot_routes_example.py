from gpx_parser import GPXParser
from gpx_plotter import GPXPlotter

# Example usage:
# Option 1: Using multiple folder paths
folder_paths = ['GPX_Files/Sabbath_Walks/Islington Park']
parser = GPXParser(folder_paths=folder_paths)

# Option 2: Using a list of GPX files
# gpx_files = ['file1.gpx', 'file2.gpx']
# parser = GPXParser(gpx_files=gpx_files)

# Option 3: Using both multiple folder paths and a list of GPX files
# folder_paths = ['/path/to/gpx/files1', '/path/to/gpx/files2']
# gpx_files = ['file1.gpx', 'file2.gpx']
# parser = GPXParser(folder_paths=folder_paths, gpx_files=gpx_files)

# Parse all the GPX files and get the routes
routes = parser.parse_all_files()

# Create a GPXPlotter instance with the parsed routes
plotter = GPXPlotter(routes)

# Create the folium map and add the routes
plotter.create_route_map()
plotter.add_routes_to_map()

# Save the map to an HTML file
plotter.save_route_map('Maps/Misc/routes_map.html')
