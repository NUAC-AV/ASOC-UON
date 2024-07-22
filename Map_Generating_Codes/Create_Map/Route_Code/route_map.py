import folium

class RouteMap:
    # Initalise varibles
    def __init__(self, all_routes, map_settings, start_markers, end_marker, route_styles):
        self.all_routes = all_routes
        self.map_settings = map_settings
        self.start_markers = start_markers
        self.end_marker = end_marker
        self.route_styles = route_styles

    # Initalise marker details
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

    # Function creates map.
    def create_map(self, output_file):
        centre, zoom = self.map_settings
        if self.all_routes and self.all_routes[0]:
            start_point = self.all_routes[0][centre]
            print(f"Start point: {start_point}")
        else:
            start_point = [0, 0]
            print("No valid routes found. Defaulting start point to [0, 0]")

        m = folium.Map(location=start_point, zoom_start=zoom)

        for route, style in zip(self.all_routes, self.route_styles):
            folium.PolyLine(route, color=style.get('color', 'blue'), weight=style.get('weight', 2.5), opacity=style.get('opacity', 1)).add_to(m)

        for route, start_marker in zip(self.all_routes, self.start_markers):
            self._add_marker_to_map(m, route[0], start_marker)

        if self.end_marker != "Ignore":
            self._add_marker_to_map(m, self.all_routes[-1][-1], self.end_marker)

        m.save(output_file)
        print(f"Map has been saved to {output_file}")

