from gpx_utils import parse_gpx_files
from route_map import RouteMap

def main():
    gpx_files = [
    'GPX_Routes/Mount_Sugarloaf_summit_walk.gpx',
    ]
    output_file = 'Maps/Sugarloaf_Walk.html'
    map_settings = (25, 17)  # Center index and zoom level
    start_markers = [
        {
            "name": "Please Park Here!",
            "link": "https://www.google.com/maps/place/Mount+Sugarloaf+Lookout/@-32.9411111,151.7239133,11z/data=!4m6!3m5!1s0x6b73393b2c49f021:0x7bc423b61a9121b6!8m2!3d-32.8910854!4d151.5381866!16s%2Fg%2F11gxmgm780?entry=ttu",
            "icon": "mountain",
            "colour": "darkgreen",
            "description": "We start from the park and heading on the loop and up the summit."
        }
    ]

    end_marker = "Ignore"

    route_styles = [
    {"color": "red", "weight": 3, "opacity": 0.8},
    ]

    all_routes = parse_gpx_files(gpx_files)
    print(f"All routes: {all_routes}")
    route_map = RouteMap(all_routes, map_settings, start_markers, end_marker, route_styles)
    route_map.create_map(output_file)


if __name__ == "__main__":
    main()