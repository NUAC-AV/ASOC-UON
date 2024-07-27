import sys
import os

# Add the directory containing gpx_parser and gpx_plotter to the Python path
sys.path.append(os.path.abspath('Map_Generating_Codes/Create_Routes'))

from gpx_parser import GPXParser
from gpx_plotter import GPXPlotter


folder_paths = ['GPX_Files/Sabbath_Walks/Hickson Street Lookout']
parser = GPXParser(folder_paths=folder_paths)


# Parse all the GPX files and get the routes
routes = parser.parse_all_files()

# Create a GPXPlotter instance with the parsed routes
plotter = GPXPlotter(routes)

# Create the folium map and add the routes
plotter.create_route_map(zoom=18)
plotter.add_routes_to_map()
link = "https://www.google.com/maps/place/Hickson+Street+Lookout/@-32.9531743,151.746488,16z/data=!3m1!4b1!4m6!3m5!1s0x6b7315d54bfbc527:0xdda9d29f3b2f085d!8m2!3d-32.9531743!4d151.746488!16s%2Fg%2F11b_25x7fp?hl=en-AU&entry=ttu"
desc = "Short 1 km walk, but very steep."
plotter.add_start_marker("Hickson Street", link, desc)

# Save the map to an HTML file
plotter.save_route_map('Maps/Sabbath_Walks/Hickson Street Lookout/routes_map.html')