import folium
import gpxpy

class RouteMap:
    def __init__(self, gpx_files, map_settings, start_markers, end_marker, route_styles):
        self.gpx_files = gpx_files
        self.map_settings = map_settings
        self.start_markers = start_markers
        self.end_marker = end_marker
        self.route_styles = route_styles
        self.all_routes = self._parse_gpx_files()

    def _parse_gpx_files(self):
        all_routes = []
        for gpx_file in self.gpx_files:
            with open(gpx_file, 'r') as f:
                gpx = gpxpy.parse(f)
                route = [(point.latitude, point.longitude) for track in gpx.tracks for segment in track.segments for point in segment.points]
                all_routes.append(route)
        return all_routes

    def _add_marker_to_map(self, map_obj, location, marker_info):
        name = marker_info.get("name", "")
        link = marker_info.get("link", "")
        icon = marker_info.get("icon", "info-sign")
        colour = marker_info.get("colour", "blue")
        description = marker_info.get("description", "")

        if icon == 'asoc':
            custom_icon_path = "Pictures/ASOC-Logo-orange.png"
            custom_icon = folium.CustomIcon(custom_icon_path, icon_size=(70, 32))
        else:
            custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')

        popup_content = f"<b>{name}</b><br>{description}"
        if link:
            popup_content = f"<b>{name}</b><br><a href='{link}' target='_blank'>Google Maps Link</a><br>{description}"

        folium.Marker(
            location=location,
            popup=popup_content,
            tooltip=name,
            icon=custom_icon
        ).add_to(map_obj)

    def create_map(self, output_file):
        centre, zoom = self.map_settings
        start_point = self.all_routes[0][centre] if self.all_routes and self.all_routes[0] else [0, 0]
        m = folium.Map(location=start_point, zoom_start=zoom)

        for route, style in zip(self.all_routes, self.route_styles):
            folium.PolyLine(route, color=style.get('color', 'blue'), weight=style.get('weight', 2.5), opacity=style.get('opacity', 1)).add_to(m)

        for route, start_marker in zip(self.all_routes, self.start_markers):
            self._add_marker_to_map(m, route[0], start_marker)

        self._add_marker_to_map(m, self.all_routes[-1][-1], self.end_marker)

        m.save(output_file)
        print(f"Map has been saved to {output_file}")

# Example usage
if __name__ == "__main__":
    gpx_files = [
    'GPX_Routes/Basden_Theatre/Science_Lane_Parking.gpx',
    'GPX_Routes/Basden_Theatre/Physics_Parking.gpx'
    ]
    output_file = 'Church_Locations/Library_Church.html'
    map_settings = (5, 35)  # Center index and zoom level
    start_markers = [
        {
            "name": "Park her for service.",
            "link": "https://www.google.com/maps/place/Parking+lot,+Callaghan+NSW+2308/@-32.892825,151.6967984,19.24z/data=!4m6!3m5!1s0x6b733fd6ed40ea51:0xd0018d02fa4ab5b9!8m2!3d-32.8926406!4d151.6967744!16s%2Fg%2F11c1j793_h?entry=ttu",
            "icon": "square-parking",
            "colour": "darkpurple",
            "description": "Parking is limited here. So please reserve it for people with food, equipment or poor mobility."
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

    route_map = RouteMap(gpx_files, map_settings, start_markers, end_marker, route_styles)
    route_map.create_map(output_file)
