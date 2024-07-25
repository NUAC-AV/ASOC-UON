import gpxpy
import os

class GPXParser:
    def __init__(self, folder_paths=None, gpx_files=None):
        """
        Initializes the GPXParser with folder paths or a list of GPX files.

        :param folder_paths: List of folder paths containing GPX files (optional)
        :param gpx_files: List of individual GPX file paths (optional)
        """
        if folder_paths is None and gpx_files is None:
            raise ValueError("Either folder_paths or gpx_files must be provided")
        self.folder_paths = folder_paths if folder_paths is not None else []
        self.gpx_files = gpx_files if gpx_files is not None else []
        self.all_routes = {}

    def get_gpx_files_from_folders(self):
        """
        Retrieves all GPX files from the specified folders.

        :return: List of GPX file paths from the folders
        """
        gpx_files = []
        for folder_path in self.folder_paths:
            gpx_files.extend([os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.gpx')])
        return gpx_files

    def parse_gpx_file(self, gpx_file):
        """
        Parses a single GPX file and extracts the route.

        :param gpx_file: Path to the GPX file
        :return: List of tuples containing latitude and longitude points
        """
        with open(gpx_file, 'r') as f:
            gpx = gpxpy.parse(f)
            route = [(point.latitude, point.longitude) for track in gpx.tracks for segment in track.segments for point in segment.points]
        return route

    def parse_all_files(self):
        """
        Parses all GPX files provided either through folder paths or as individual files.
        Stores the routes in a dictionary with keys named after the filenames (underscores replaced with spaces).

        :return: Dictionary of routes with filenames as keys
        """
        # If folder paths are provided, get the GPX files from the folders
        if self.folder_paths:
            self.gpx_files.extend(self.get_gpx_files_from_folders())

        # Parse each GPX file and store the route in the dictionary
        for gpx_file in self.gpx_files:
            route = self.parse_gpx_file(gpx_file)
            # Create a key name from the file name by replacing underscores with spaces and removing the '.gpx' extension
            file_name = os.path.basename(gpx_file).replace('_', ' ').replace('.gpx', '')
            self.all_routes[file_name] = route

        return self.all_routes



# Example usage:
gpx_files = ['GPX_Files/Sabbath_Walks/Islington Park/Throsby_Creek_Walk.gpx']
parser = GPXParser(gpx_files=gpx_files)
all_routes = parser.parse_all_files()
print(all_routes)
