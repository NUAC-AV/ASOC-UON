from Map_Generating_Codes.Create_Routes.gpx_parser import parse_gpx_files
from route_map import RouteMap

def main():
    gpx_files = [
    'GPX_Routes/Basden_Theatre/Science_Lane_Parking.gpx',
    'GPX_Routes/Basden_Theatre/Physics_Parking.gpx'
    ]
    output_file = 'Church_Locations/Library_Church.html'
    map_settings = (5, 35)  # Center index and zoom level
    start_markers = [
        {
            "name": "Parking is limited!",
            "link": "https://www.google.com/maps/place/Parking+lot,+Callaghan+NSW+2308/@-32.892825,151.6967984,19.24z/data=!4m6!3m5!1s0x6b733fd6ed40ea51:0xd0018d02fa4ab5b9!8m2!3d-32.8926406!4d151.6967744!16s%2Fg%2F11c1j793_h?entry=ttu",
            "icon": "square-parking",
            "colour": "darkpurple",
            "description": "Please reserve it for people with food, equipment or poor mobility."
        },
        {
            "name": "Please Park here",
            "link": "https://www.google.com/maps/place/Parking+lot,+Callaghan+NSW+2308/@-32.8930431,151.6966156,19.03z/data=!4m6!3m5!1s0x6b733fd69f626e5d:0xfd63acc8e85cad8d!8m2!3d-32.8936394!4d151.6962264!16s%2Fg%2F11c0vp7ggl?entry=ttu",
            "icon": "square-parking",
            "colour": "darkpurple",
            "description": "Follow route to church service."
        }
    ]

    end_marker = {
        "name": "Church",
        "icon": "asoc",
        "colour": "red",
        "description": "Church"
    }

    route_styles = [
    {"color": "red", "weight": 3, "opacity": 0.8},
    {"color": "blue", "weight": 3, "opacity": 1}
    ]

    all_routes = parse_gpx_files(gpx_files)
    print(f"All routes: {all_routes}")
    route_map = RouteMap(all_routes, map_settings, start_markers, end_marker, route_styles)
    route_map.create_map(output_file)


if __name__ == "__main__":
    main()