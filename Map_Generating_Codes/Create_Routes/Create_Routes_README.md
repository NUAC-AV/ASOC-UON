# GPX Route Plotter

1. `GPXParser` - For parsing GPX files and extracting route information.
2. `GPXPlotter` - For plotting the parsed routes on a folium map.


## Features

- Parse multiple GPX files from directories or a list of file paths.
- Plot routes on an interactive map with folium.
- Add markers for the start and end points of each route.
- Save the interactive map as an HTML file.
- Organize routes and markers into feature groups for better visualization.

## Documentation

### GPXParser

- __init__(self, folder_paths=None, gpx_files=None): Initializes the GPXParser with folder paths or a list of GPX files.
  - Parameters:
    - folder_paths (list, optional): List of folder paths containing GPX files.
    - gpx_files (list, optional): List of individual GPX file paths.
  - Raises:
    - ValueError: If neither folder_paths nor gpx_files is provided.

- get_gpx_files_from_folders(self): Retrieves all GPX files from the specified folders.
  - Returns:
    - list: List of GPX file paths from the folders.

- parse_gpx_file(self, gpx_file): Parses a single GPX file and extracts the route.
  - Parameters:
    - gpx_file (str): Path to the GPX file.
  - Returns:
    - list: List of tuples containing latitude and longitude points.

- parse_all_files(self): Parses all GPX files provided either through folder paths or as individual files. Stores the routes in a dictionary with keys named after the filenames (underscores replaced with spaces).
  - Returns:
    - dict: Dictionary of routes with filenames as keys.

### GPXPlotter

- __init__(self, routes): Initializes the GPXPlotter with a dictionary of routes.
  - Parameters:
    - routes (dict): Dictionary of routes with filenames as keys.

- create_route_map(self): Creates a folium map centered on the first route's first point.
  - Returns:
    - folium.Map: A folium Map object.
  - Raises:
    - ValueError: If no routes are available to plot.

- add_routes_to_map(self): Adds route polylines to the folium map using feature groups.

- add_markers_to_map(self): Adds start and end markers to the folium map using feature groups.

- save_route_map(self, file_name='routes_map.html'): Saves the folium map to an HTML file.
  - Parameters:
    - file_name (str): Name of the file to save the map (default is 'routes_map.html').
