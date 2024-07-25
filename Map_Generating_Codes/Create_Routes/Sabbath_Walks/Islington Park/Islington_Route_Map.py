import sys
import os

# Add the directory containing gpx_parser and gpx_plotter to the Python path
sys.path.append(os.path.abspath('Map_Generating_Codes/Create_Routes'))

from gpx_parser import GPXParser
from gpx_plotter import GPXPlotter


folder_paths = ['GPX_Files/Sabbath_Walks/Islington Park']
parser = GPXParser(folder_paths=folder_paths)


# Parse all the GPX files and get the routes
routes = parser.parse_all_files()

# Create a GPXPlotter instance with the parsed routes
plotter = GPXPlotter(routes)

# Create the folium map and add the routes
plotter.create_route_map(zoom=17)
plotter.add_routes_to_map()
link = "https://www.google.com/maps/place/Islington+Park+Cricket+Ground,+63+Power+St,+Islington+NSW+2296/data=!4m2!3m1!1s0x6b7314553fba44e5:0x4df60ded56ec74c7?utm_source=mstt_1&entry=gps&g_ep=CAESCTExLjc4LjMwMRgAINeCAyoAQgJBVQ%3D%3D"
desc = "3 km walk with posible 1 km extention through Tighes Hill Dog Park."
plotter.add_start_marker("Islington Park", link, desc)

# Save the map to an HTML file
plotter.save_route_map('Maps/Sabbath_Walks/Islington Park/routes_map.html')