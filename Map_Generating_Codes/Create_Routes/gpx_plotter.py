import folium

class GPXPlotter:
    def __init__(self, routes):
        """
        Initializes the GPXPlotter with a dictionary of routes.
        :param routes: Dictionary of routes with filenames as keys
        """
        self.routes = routes
        self.route_map = None


    def create_route_map(self):
        """
        Creates a folium map centered on the first route's first point.
        :return: A folium Map object
        """
        if not self.routes:
            raise ValueError("No routes available to plot.")

        # Center the map on the first route's first point
        first_route = next(iter(self.routes.values()))
        map_center = first_route[0] if first_route else (0, 0)
        self.route_map = folium.Map(location=map_center, zoom_start=14)


    def add_all_routes_to_map(self):
        """
        Adds routes to the folium map.
        """
        if self.route_map is None:
            self.create_route_map()

        for route_name, route in self.routes.items():
            feature_group = folium.FeatureGroup(name=route_name)
            folium.PolyLine(route, color='blue', weight=2.5, opacity=1).add_to(feature_group)
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
