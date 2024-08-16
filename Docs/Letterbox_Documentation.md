# Letterbox Codebase Documentation

## Overview

The Letterbox project is designed to generate interactive maps with custom layers and routes. The project is organized into multiple Python modules, each responsible for a specific aspect of map generation and customization. This documentation provides an overview of the codebase, explaining the purpose and functionality of each module.

## Project Structure

- [Letterbox](../Letterbox/)
    - [suburb_manager.py](../Letterbox/suburb_manager.py)
    - [font_manager.py](../Letterbox/font_manager.py)
    - [map_utils.py](../Letterbox/map_utils.py)
    - [layer_manager.py](../Letterbox/layer_manager.py)
    - [create_map.py](../Letterbox/create_map.py)
    - [Update_Letterbox_map.py](../Letterbox/Update_Letterbox_map.py)


## Files


### `suburb_manager.py`
- **Purpose**: Manages the initialization, retrieval, and manipulation of suburb data. The `SuburbManager` class handles the geocoding of suburbs, calculation of zoom levels, and extraction of relevant features.

**Functions**:
  - `initialize_suburbs()`: 
    - **Called by**: `CreateMap.__init__()`
    - **Description**: Initializes suburb data including names, geojson, centroids, zoom levels, and regions.
  - `calculate_zoom_level(geometry, map_width_px=800, map_height_px=600, zoom_bias=2.5)`: 
    - **Called by**: `initialize_suburbs()`
    - **Description**: Calculates the appropriate zoom level for a given suburb based on its geometry.
  - `extract_suburb_data(html_content)`: 
    - **Called by**: `CreateMap.save_map()`
    - **Description**: Extracts feature groups from the HTML content and assigns them to the corresponding suburbs.
  - `get_suburb_info()`: 
    - **Called by**: `CreateMap.save_map()`
    - **Description**: Returns the list of all suburb data, including centroids, zoom levels, and regions.
  
---
### `font_manager.py`
- **Purpose**: Contains the `FontManager` class, which manages and standardizes the font styles, symbols, and labels used throughout the map. This class allows for consistent formatting and easy adjustments.

  **Functions**:
  - `get_header_font(text, color='black')`: 
    - **Called by**: `CreateMap.__init__()`, `Update_Letterbox_map.py`.
    - **Description**: Returns a formatted string for a header with the specified text and color.
  - `get_subheader_font(text, color='black')`: 
    - **Called by**: `LayerManager.add_layers()`.
    - **Description**: Returns a formatted string for a subheader with the specified text and color.
  - `get_label_font(text, color='black')`: 
    - **Called by**: `LayerManager.add_layers()`.
    - **Description**: Returns a formatted string for a label with the specified text and color.
  - `get_closed_symbol(symbol='&#9654;', color='black', size='18px')`: 
    - **Called by**: `CreateMap.add_tree_layer_control()`
    - **Description**: Returns a formatted string for a closed symbol with the specified properties.
  - `get_opened_symbol(symbol='&#9662;', color='black', size='18px')`: 
    - **Called by**: `CreateMap.add_tree_layer_control()`
    - **Description**: Returns a formatted string for an opened symbol with the specified properties.
  - `get_collapse_all_label(color='black')`: 
    - **Called by**: `CreateMap.add_tree_layer_control()`
    - **Description**: Returns a formatted string for the "Collapse all" label with the specified color.
  - `get_expand_all_label(color='black')`: 
    - **Called by**: `CreateMap.add_tree_layer_control()`
    - **Description**: Returns a formatted string for the "Expand all" label with the specified color.

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
  - `add_css(map_object)`: 
    - **Called by**: `CreateMap.apply_custom_css()`
    - **Description**: Injects custom CSS styles into the Folium map to modify the appearance of various map elements.
  - `post_process_html(filename)`: 
    - **Called by**: `CreateMap.save_map()`
    - **Description**: Post-processes the generated HTML file by removing the last five lines and adding the correct content, ensuring that the symbols and formatting are consistent.

---
### `layer_manager.py`
- **Purpose**: Features the `LayerManager` class, responsible for adding and organizing layers on the map. It processes places and regions, adjusts colors, and integrates layers into the map’s overlay structure.

**Functions**:
  - `add_layers()`: 
    - **Called by**: `CreateMap.__init__()`
    - **Description**: Manages the process of creating and adding layers for regions and suburbs to the map, including color adjustments.
  - `add_gpx_route(gpx_file, layer_name="GPX Route", color='blue', show=True)`: 
    - **Called by**: `LayerManager.add_gpx_routes()`
    - **Description**: Adds a single GPX route to the map as a layer with customizable options.
  - `add_gpx_routes(folder_path, color='black', show=True)`: 
    - **Called by**: The main script in `Update_Letterbox_map.py`.
    - **Description**: Adds multiple GPX routes from a specified folder to the map.
  - `get_gpx_layers()`: 
    - **Called by**: The main script in `Update_Letterbox_map.py` to retrieve layers for integration into `CreateMap`.
    - **Description**: Returns the list of GPX layers that have been added to the map.

    
---
### `create_map.py`
- **Purpose**: The core class `CreateMap` integrates all components to manage map creation, setup layers, and apply custom styles. This class drives the entire process of generating and saving the interactive map.

**Functions**:
  - `__init__(base_places, gpx_folder, map_location=(-32.9, 151.79), zoom_start=12)`: 
    - **Calls**: `LayerManager.__init__()`, `SuburbManager.__init__()`
    - **Description**: Initializes the map object, sets up base places, manages layers, and prepares the overlay tree structure.
  - `apply_custom_css()`: 
    - **Calls**: `MapUtils.add_css()`
    - **Description**: Applies custom CSS styles to the map.
  - `add_tree_layer_control()`: 
    - **Calls**: `FontManager.get_closed_symbol()`, `FontManager.get_opened_symbol()`, `FontManager.get_collapse_all_label()`, `FontManager.get_expand_all_label()`
    - **Description**: Adds a tree layer control to the map, applying custom CSS and replacing labels with images if necessary.
  - `setup_map()`: 
    - **Calls**: `apply_custom_css()`, `add_tree_layer_control()`
    - **Description**: Configures the map with all layers, controls, and custom styles.
  - `initialize_map(output_html)`: 
    - **Description**: Initializes and saves the map to an HTML file.
  - `save_map(output_html)`: 
    - **Description**: Saves the map and modifies the saved HTML file to inject additional JavaScript and CSS.



---
### `Update_Letterbox_map.py`
- **Purpose**: The entry point script for generating the Letterbox map. It encapsulates the entire map generation process within the `UpdateLetterboxMap` class. This script sets up base places, adds GPX routes, integrates layers, and saves the final map as an HTML file. Additionally, it applies custom CSS for post-processing.

**Main Class**:
  - **UpdateLetterboxMap**: Manages the map generation process, coordinating the creation of the map, addition of GPX routes, integration of layers, saving of the map, and application of custom CSS.

**Key Methods**:
  - `create_map`: Initializes the map with `CreateMap` using base places.
  - `save_map`: Saves the map as an HTML file.
  - `run`: Executes the entire map generation process.

**Class Calls**:
  - `UpdateLetterboxMap(base_places, gpx_folder, output_html)`: Creates an instance of the `UpdateLetterboxMap` class.
  - `app.run()`: Executes the entire map generation process.

---


## Test Letterbox Maps
**Map number.**
- 11:  
- 12: Used down(red) and right(green) arrows for closed and open symbols respectively.
- 13: 
  | header | subheader | label | 
  | :---:  | :-------: | :---: |
  | 16     | 14        | 12    |
  Collaspe all text red  
  Expand all text green
- 14:
  | header | subheader | label | 
  | :---:  | :-------: | :---: |
  | 14     | 14        | 14    |
- 15: 
  width: 250, height: 250
- 16:
  width: 3300, height: 280, removed zoom bar
- 17:
  Add recenter after clicking on region.


## UML Diagram

![Letterbox Diagram](/Images/UML_Diagrams/Letterbox_Code_UML.svg)


