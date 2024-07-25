import folium

class GPXPlotter:
    def __init__(self, routes):
        """
        Initializes the GPXPlotter with a dictionary of routes.
        :param routes: Dictionary of routes with filenames as keys
        """
        self.routes = routes
        self.route_map = None


    def create_route_map(self, zoom):
        """
        Creates a folium map centered on the first route's first point.
        :return: A folium Map object
        """
        if not self.routes:
            raise ValueError("No routes available to plot.")

         # Calculate the center of the first route
        first_route = next(iter(self.routes.values()))
        if first_route:
            avg_lat = sum(point[0] for point in first_route) / len(first_route)
            avg_lon = sum(point[1] for point in first_route) / len(first_route)
            map_center = (avg_lat, avg_lon)
        else:
            map_center = (0, 0)
        self.route_map = folium.Map(location=map_center, zoom_start=zoom)


    def add_routes_to_map(self):
        """
        Adds routes to the folium map.
        """
        if self.route_map is None:
            self.create_route_map()

        for route_name, route in self.routes.items():
            feature_group = folium.FeatureGroup(name=route_name)
            folium.PolyLine(route, color='blue', weight=2.5, opacity=1).add_to(feature_group)
            feature_group.add_to(self.route_map)

    def add_start_marker(self, name, link, desc):
        """
        Adds start marker.

        :param name: Name for the tooltip.
        :param link: URL to be included in the marker popup.
        :param desc: Description to be included in the marker popup.
        """
        if self.route_map is None:
            self.create_route_map()

        # Define the link
        marker_link = f"<a href='{link}' target='_blank'>Google Map Link</a>"

        for route_name, route in self.routes.items():
            feature_group = folium.FeatureGroup(name=f'{route_name} Markers')
            folium.Marker(route[0],
                          popup=f'<b>{route_name}<b><br>{marker_link}<br>{desc}',
                          tooltip=name).add_to(feature_group)
            #folium.Marker(route[-1], popup=f'{route_name} End').add_to(feature_group)
            feature_group.add_to(self.route_map)

        
    def add_markers_to_map(self):
        """
        Adds start and end markers to the folium map using feature groups.
        """
        if self.route_map is None:
            self.create_route_map()

        for route_name, route in self.routes.items():
            feature_group = folium.FeatureGroup(name=f'{route_name} Markers')
            folium.Marker(route[0], popup=f'{route_name} Start').add_to(feature_group)
            folium.Marker(route[-1], popup=f'{route_name} End').add_to(feature_group)
            feature_group.add_to(self.route_map)


    def save_route_map(self, file_name='routes_map.html'):
        """
        Saves the folium map to an HTML file.

        :param file_name: Name of the file to save the map (default is 'routes_map.html')
        """
        if self.route_map is None:
            self.create_route_map()
            self.add_routes_to_map()
            self.add_markers_to_map()
        folium.LayerControl().add_to(self.route_map)
        self.route_map.save(file_name)
