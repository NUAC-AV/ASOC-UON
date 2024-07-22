# Map Generating Codes


## 📚 Table of Contents
- [Overview](#overview)
- [Subfolders](#subfolders)
- [Files](#files)



## Overview.
This folder contains all the python code for generating maps.


## Subfolders and files
- **Create_Routes**:Creates a route.
- **Letterbox**: Creates the letterbox maps.
- **Misc**: 
- **Route_Code**: 
- **README.md**: 
- **Update_Walks.py**: Updates the map of ASOC walks

## Files
- gpx_utils.py: reads the gpx file.
- route_map.py: Class of methods for map making.
    - __init__(self, all_routes, map_settings, start_markers, end_marker, route_styles)
    - _add_marker_to_map(self, map_obj, location, marker_info)
    - create_map(self, output_file)
- main.py: Runs the code for map making.
