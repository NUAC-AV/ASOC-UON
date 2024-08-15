# Letterbox Codebase Documentation

## Overview

The Letterbox project is designed to generate interactive maps with custom layers and routes. The project is organized into multiple Python modules, each responsible for a specific aspect of map generation and customization. This documentation provides an overview of the codebase, explaining the purpose and functionality of each module.

## Project Structure

- [Letterbox](../Letterbox/)
    - [custom_css.py](../Letterbox/custom_css.py)
    - [font_manager.py](../Letterbox/font_manager.py)
    - [gpx_handler.py](../Letterbox/gpx_handler.py)
    - [layer_manager.py](../Letterbox/layer_manager.py)
    - [map_utils.py](../Letterbox/map_utils.py)
    - [tree_layer_control.py](../Letterbox/tree_layer_control.py)
    - [Update_Letterbox_map.py](../Letterbox/Update_Letterbox_map.py)

## Files

### `custom_css.py`
- **Purpose**: Contains the `CustomCSS` class, which adds custom CSS styles and post-processes the generated HTML map file. It customizes the appearance of map elements like layer controls, buttons, and labels.

  **Functions**:
  - `add_css()`: 
    - **Called by**: `MapWithTreeLayerControl.add_tree_layer_control()`
    - **Description**: Injects custom CSS styles into the Folium map to modify the appearance of various map elements.
  - `post_process_html(filename)`:
    - **Called by**: The main script after `MapWithTreeLayerControl.save_map()`.
    - **Description**: Post-processes the generated HTML file by removing the last five lines and adding the correct content, ensuring that the symbols and formatting are consistent.


---
### `gpx_handler.py`
- **Purpose**: Includes the `GPXHandler` class for managing GPX routes on the map. It allows the addition of GPX files as layers, with options for customizing route appearance and visibility.

**Functions**:
  - `add_gpx_route(gpx_file, layer_name="GPX Route", color='blue', show=True)`:
    - **Called by**: `GPXHandler.add_gpx_routes()`
    - **Description**: Adds a single GPX route to the map as a layer with customizable options.
  - `add_gpx_routes(folder_path, color='black', show=True)`:
    - **Called by**: The main script in `Update_Letterbox_map.py`.
    - **Description**: Adds multiple GPX routes from a specified folder to the map.
  - `get_gpx_layers()`:
    - **Called by**: The main script in `Update_Letterbox_map.py` to retrieve layers for integration into `MapWithTreeLayerControl`.
    - **Description**: Returns the list of GPX layers that have been added to the map.


---
### `layer_manager.py`
- **Purpose**: Features the `LayerManager` class, responsible for adding and organizing layers on the map. It processes places and regions, adjusts colors, and integrates layers into the map’s overlay structure.

**Functions**:
  - `add_layers()`:
    - **Called by**: `MapWithTreeLayerControl.__init__()`
    - **Description**: Manages the process of creating and adding layers for regions and suburbs to the map, including color adjustments.


---
### `map_utils.py`
- **Purpose**: Provides utility functions via the `MapUtils` class. This includes methods for adjusting color properties and geocoding place names, which are used by other classes for map customization.

**Functions**:
  - `adjust_brightness(color, factor)`:
    - **Called by**: `LayerManager.add_layers()`
    - **Description**: Adjusts the brightness of a given color by the provided factor.
  - `adjust_hue(color, hue_factor)`:
    - **Called by**: `LayerManager.add_layers()`
    - **Description**: Adjusts the hue of a given color by the provided factor.
  - `geocode_places(base_places, location="Newcastle, Australia")`:
    - **Called by**: `LayerManager.__init__()`
    - **Description**: Geocodes a list of places to their geographical coordinates.


---
### `tree_layer_control.py`
- **Purpose**: The main file that manages map creation. The `MapWithTreeLayerControl` class integrates all components, handles map setup, layer addition, and applies custom styles, resulting in the final interactive map.

**Functions**:
  - `__init__(base_places, map_location=(-32.9, 151.79), zoom_start=12)`:
    - **Calls**: `LayerManager.add_layers()`
    - **Description**: Initializes the map object, sets up base places, and prepares the overlay tree structure.
  - `add_tree_layer_control()`:
    - **Calls**: `CustomCSS.add_css()`, `FontManager.get_closed_symbol()`, `FontManager.get_opened_symbol()`, `FontManager.get_collapse_all_label()`, `FontManager.get_expand_all_label()`.
    - **Description**: Adds a tree layer control to the map, applying custom CSS and replacing labels with images if necessary.
  - `save_map(output_html)`:
    - **Description**: Saves the generated map to an HTML file.
    - **Followed by**: `CustomCSS.post_process_html()` in the main script.


---
### `font_manager.py`
- **Purpose**: Contains the `FontManager` class, which manages and standardizes the font styles, symbols, and labels used throughout the map. This class allows for consistent formatting and easy adjustments.

**Functions**:
  - `get_header_font(text, color='black')`:
    - **Called by**: `MapWithTreeLayerControl.__init__()`, `Update_Letterbox_map.py`.
    - **Description**: Returns a formatted string for a header with the specified text and color.
  - `get_subheader_font(text, color='black')`:
    - **Called by**: `LayerManager.add_layers()`.
    - **Description**: Returns a formatted string for a subheader with the specified text and color.
  - `get_label_font(text, color='black')`:
    - **Called by**: `LayerManager.add_layers()`.
    - **Description**: Returns a formatted string for a label with the specified text and color.
  - `get_closed_symbol(symbol='&#9654;', color='black', size='18px')`:
    - **Called by**: `MapWithTreeLayerControl.add_tree_layer_control()`
    - **Description**: Returns a formatted string for a closed symbol with the specified properties.
  - `get_opened_symbol(symbol='&#9662;', color='black', size='18px')`:
    - **Called by**: `MapWithTreeLayerControl.add_tree_layer_control()`
    - **Description**: Returns a formatted string for an opened symbol with the specified properties.
  - `get_collapse_all_label(color='black')`:
    - **Called by**: `MapWithTreeLayerControl.add_tree_layer_control()`
    - **Description**: Returns a formatted string for the "Collapse all" label with the specified color.
  - `get_expand_all_label(color='black')`:
    - **Called by**: `MapWithTreeLayerControl.add_tree_layer_control()`
    - **Description**: Returns a formatted string for the "Expand all" label with the specified color.

---
### `Update_Letterbox_map.py`
- **Purpose**: The entry point script for generating the Letterbox map. It encapsulates the entire map generation process within the `MapApplication` class. This script sets up base places, adds GPX routes, integrates layers, and saves the final map as an HTML file. Additionally, it applies custom CSS for post-processing.

**Main Class**:
  - **MapApplication**: Manages the map generation process, coordinating the creation of the map, addition of GPX routes, integration of layers, saving of the map, and application of custom CSS.

**Key Methods**:
  - **create_map**: Initializes the map with `MapWithTreeLayerControl` using base places.
  - **add_gpx_routes**: Loads and adds GPX routes to the map using `GPXHandler`.
  - **integrate_gpx_layers**: Integrates the GPX layers into the map.
  - **add_tree_layer_control**: Adds the tree layer control to the map.
  - **save_map**: Saves the map as an HTML file.
  - **apply_custom_css**: Applies custom CSS post-processing to the saved HTML file using `CustomCSS`.

**Class Calls**:
  - `MapApplication(base_places, gpx_folder, output_html)`: Creates an instance of the `MapApplication` class.
  - `app.run()`: Executes the entire map generation process.

---

## Test Letterbox Maps
**Map number.**
- 11:  
- 12: Used down and right arrows for 

## UML Diagram

![Letterbox Diagram](/Images/Letterbox_Diagram.svg)


