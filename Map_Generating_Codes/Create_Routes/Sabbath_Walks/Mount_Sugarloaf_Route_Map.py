import sys
import os

# Add the directory containing gpx_parser and gpx_plotter to the Python path
sys.path.append(os.path.abspath('Map_Generating_Codes/Create_Routes'))

from gpx_parser import GPXParser
from gpx_plotter import GPXPlotter


folder_paths = ['GPX_Files/Sabbath_Walks/Mount Sugarloaf']
parser = GPXParser(folder_paths=folder_paths)


# Parse all the GPX files and get the routes
routes = parser.parse_all_files()

# Create a GPXPlotter instance with the parsed routes
plotter = GPXPlotter(routes)

# Create the folium map and add the routes
plotter.create_route_map(zoom=17)
plotter.add_routes_to_map()
link = "https://www.google.com/maps/place/Mount+Sugarloaf+Lookout/@-32.9411111,151.7239133,11z/data=!4m6!3m5!1s0x6b73393b2c49f021:0x7bc423b61a9121b6!8m2!3d-32.8910854!4d151.5381866!16s%2Fg%2F11gxmgm780?entry=ttu"
desc = "We start from the park and heading on the loop and up the summit."
plotter.add_start_marker("Mount Sugarloaf", link, desc)

# Save the map to an HTML file
plotter.save_route_map('Maps/Sabbath_Walks/Mount_Sugarloaf.html')