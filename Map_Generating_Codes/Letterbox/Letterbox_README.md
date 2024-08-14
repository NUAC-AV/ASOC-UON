# Letterbox Codebase Documentation

## Overview

The Letterbox project is designed to generate interactive maps with custom layers and routes. The project is organized into multiple Python modules, each responsible for a specific aspect of map generation and customization. This documentation provides an overview of the codebase, explaining the purpose and functionality of each module.

## Project Structure

- [Letterbox](../Letterbox/)
    - [custom_css.py](../Letterbox/custom_css.py)
    - [gpx_handler.py](../Letterbox/gpx_handler.py)
    - [layer_manager.py](../Letterbox/layer_manager.py)
    - [map_utils.py](../Letterbox/map_utils.py)
    - [tree_layer_control.py](../Letterbox/tree_layer_control.py)
    - [Update_Letterbox_map.py](../Letterbox/Update_Letterbox_map.py)

## Files

### `custom_css.py`
- **Purpose**: Contains the `CustomCSS` class, which adds custom CSS styles to the interactive map. It customizes the appearance of map elements like layer controls, buttons, and labels.

  **Functions**:
  - `add_css()`: Injects custom CSS styles into the Folium map to modify the appearance of various map elements.


---
### `gpx_handler.py`
- **Purpose**: Includes the `GPXHandler` class for managing GPX routes on the map. It allows the addition of GPX files as layers, with options for customizing route appearance and visibility.

**Functions**:
  - `add_gpx_route(gpx_file, layer_name="GPX Route", color='blue', show=True)`: Adds a single GPX route to the map as a layer with customizable options.
  - `add_gpx_routes(folder_path, color='black', show=True)`: Adds multiple GPX routes from a specified folder to the map.
  - `get_gpx_layers()`: Returns the list of GPX layers that have been added to the map.


---
### `layer_manager.py`
- **Purpose**: Features the `LayerManager` class, responsible for adding and organizing layers on the map. It processes places and regions, adjusts colors, and integrates layers into the map’s overlay structure.

**Functions**:
  - `add_layers()`: Manages the process of creating and adding layers for regions and suburbs to the map, including color adjustments.


---
### `map_utils.py`
- **Purpose**: Provides utility functions via the `MapUtils` class. This includes methods for adjusting color properties and geocoding place names, which are used by other classes for map customization.

**Functions**:
  - `adjust_brightness(color, factor)`: Adjusts the brightness of a given color by the provided factor.
  - `adjust_hue(color, hue_factor)`: Adjusts the hue of a given color by the provided factor.
  - `geocode_places(base_places, location="Newcastle, Australia")`: Geocodes a list of places to their geographical coordinates.


---
### `tree_layer_control.py`
- **Purpose**: The main file that manages map creation. The `MapWithTreeLayerControl` class integrates all components, handles map setup, layer addition, and applies custom styles, resulting in the final interactive map.

**Functions**:
  - `__init__(base_places, map_location=(-32.9, 151.79), zoom_start=12)`: Initializes the map object, sets up base places, and prepares the overlay tree structure.
  - `add_tree_layer_control()`: Adds a tree layer control to the map, applying custom CSS and replacing labels with images if necessary.
  - `save_map(output_html)`: Saves the generated map to an HTML file.


---
### `Update_Letterbox_map.py`
- **Purpose**: The entry point script for generating the Letterbox map. It combines all modules, sets up base places, adds GPX routes, integrates layers, and saves the final map as an HTML file.

**Functions**:
  - This file primarily runs the necessary classes and methods from the other modules to generate and save the map. It does not define new functions but orchestrates the use of the existing ones.s
