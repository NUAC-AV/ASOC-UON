# Interactive Map from Google Sheets

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install Required Libraries](#install-required-libraries)
  - [Folder Structure](#folder-structure)
  - [Icon Colors and Symbols](#icon-colors-and-symbols)
- [Running Code](#running-code)
- [Usage](#usage)
  - [Clone the Repository](#clone-the-repository)
  - [Run the Script](#run-the-script)
  - [View the Map](#view-the-map)
- [Google Sheet Structure](#google-sheet-structure)
  - [Example Google Sheet](#example-google-sheet)
- [Notes](#notes)
- [License](#license)

## Overview
This project provides Python scripts to read data from an ASOC_Walks_Database Google Sheets document, which is used to create an interactive map with markers using the `folium` library. The map is saved as an HTML file, which can be viewed in any web browser.

[Google Sheets Document](https://docs.google.com/spreadsheets/d/1mGR_xugxcg3Pc3e1KLzggZn6XfnSJOuHncZ64hOo8M4/edit?fbclid=IwZXh0bgNhZW0CMTAAAR3rcnaz2qedGxf1LaI0fz7X7gUQiZrvZTjs3x-MfPTNZODKO8ykz3piWDI_aem_mtzQRofiQxsPinF7C6uSHg&gid=0#gid=0)

## Features
- Read data from "ASOC_Walks_Database"
- Create an interactive map from the database
- Add markers for each location with popups containing relevant information
- Save the map as an HTML file


## Requirements
- Python 3.x
- `pandas` library
- `folium` library
- `gpxpy` library
- `pdf2image` library
- `Pillow` library


## Setup



## Example Google Sheet
| Location | Latitude | Longitude | Google_Link | Address | Discription | Route_Link  | Icon | Color |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|Awabakal Nature Reserve  | -32.99149503 | 151.7222826  | [Link](https://www.google.com/maps/place/13+Ivy+St,+Dudley+NSW+2290/data=!4m6!3m5!1s0x6b7317ca43cdc65d:0x6eedd6577b803386!7e2!8m2!3d-32.9917425!4d151.7222826?utm_source=mstt_1&entry=gps&lucs=,47075915&g_ep=CAESCjExLjEwOS4xMDEYACDXggMqCSw0NzA3NTkxNUICQVU%3D)   | 13 Ivy St, Dudley NSW 2290      | It will be in the bush, so please have proper walking shoes for the walk. We can park on the road around Ivy Street. | [link](file:///Users/roryyarr/Desktop/ASOC%20Walks/Maps/ASOC_walk_locations_map.html) | tree  | green |
| Bar Beach  | -32.94047053 | 151.7695674  | [Link](https://www.google.com/maps/place/Yuelarbah+Track,+Bar+Beach+NSW+2300/@-32.9406461,151.764718,946m/data=!3m2!1e3!4b1!4m15!1m8!3m7!1s0x6b73143fbd4c9111:0x5017d681632e890!2sBar+Beach+NSW+2300!3b1!8m2!3d-32.9377866!4d151.7701917!16s%2Fm%2F02x66br!3m5!1s0x6b73143e338a20c5:0xbac9ffd0659c571a!8m2!3d-32.9406507!4d151.7695889!16s%2Fg%2F11m_lcwt1h?entry=ttu) | Yuelarbah Track, Bar Beach NSW 2300 |  |  | umbrella-beach | beige |
| ⋮  | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮  | ⋮  |


### Google Sheet Structure
- **Name**: The name of the location.
- **Latitude**: The latitude of the location.
- **Longitude**: The longitude of the location.
- **Google_Link**: A Google Maps link or other relevant URL.
- **Address**: The address of the location.
- **Description**: A description of the location or any additional notes.
- **Route_Link**: A link to the route map for that location.
- **Icon**: The icon to use for the marker.
- **Colour**: The color of the marker.
|  Icon  |  Colour  |  Discription  |
| :----: | :------: | :-----------: |
| `water` | `blue` | Used for river and lakes.(Exluding Saltwater.) |
| `leaf-wilt` | `lightgreen` | Used for wtlands. |
| tree | green | Used for forrests and parks. |
| umbrella-beach | beigh | For beaches and other sandy enviroments | 
| Mountain | darkgreen | For hilly and mountainous walks. |
| sailboat | pink | For Boat ramps | 
| Ferry and Ship | black | Used for other habour/coastal walks. | 
| Flag | red | Other walks not listed | 


#### Odd styling
- **Tree**: Forested area
  - *`Mountain`*: Hills or mountainous region
  - *`Leaf-wilt`*: Wetlands
  - *`Ship`*: Maritime area with large vessels
  - *`Ferry`*: Ferry routes or terminals
  - *`Sailboat`*: Boat ramps
  - *`umbrella-beach`*: Beaches
  - *`Water`*: Bodies of water such as lakes or rivers
  - *`Flag`*: Other locations
**Colour**: The color of the marker.
  - *`blue`*: Rivers or lakes 
  - *`beigh`*: Sandy areas
  - *`lightgreen`: Wetlands
  - *`green`:* Trees and forrests
  - *`darkgreen`*: Mountains and hills
  - *`pink`:* For boat ramps
  - *`black`:* For other locations


### Folder Structure
- **Church_Locations**: Contains location data.
- **GPX_Routes**: Contains GPX route files.
- **Map_Python_Codes**: Contains Python files for mapping.
  - *`Update_Walks_file.py`*: Updates the ASOC_walk_locations_map.html file with the current Google Sheets data.
  - *`Create_Routes_map.py`*: Creates a map for a route.
  - *`Create_Route_UI.py`*: Script for creating routes with a user interface.
- **Maps**: Contains the HTML files for the maps.
- **Pictures**: Contains all pictures used as logos.
- **ASOC_Walks.ipynb**: Jupyter notebook for code testing.
- **README.md**: Explains the project.


### Icon Colors and Symbols
The available colors for icons are: `black`, `beige`, `lightblue`, `gray`, `blue`, `darkred`, `lightgreen`, `purple`, `red`, `green`, `lightred`, `white`, `darkblue`, `darkpurple`, `cadetblue`, `orange`, `pink`, `lightgray`, `darkgreen`.

More details can be found [here](https://www.kaggle.com/code/aungdev/colors-available-for-marker-icons-in-folium).

Icons can be chosen from [Font Awesome](https://fontawesome.com/search?o=r&m=free). Additionally, PNG files can be used as icons.


### Install Required Libraries
Make sure you have the required libraries installed. You can install these libraries using `pip`:
- pip install folium
- pip install pandas
- pip install gpxpy
- pip install pdf2image pillow


## Usage

The maps can be viewed through GitHub Pages. You can access them using the following link format:
https://roryyarr.github.io/ASOC-Walks/`file-name`.html

Replace `file-name` with the specific file you want to view.


### Example Usages

Here are some example usages of the maps:

1. **Main ASOC Walk Locations Map**:
   - **Description**: This map shows the main locations for the ASOC walks.
   - **Link**: https://roryyarr.github.io/ASOC-Walks/Maps/ASOC_walk_locations_map.html

2. **Mount Sugarloaf Map**:
   - **Description**: This map highlights the route for the mount Sugarloaf walk.
   - **Link**: https://roryyarr.github.io/ASOC-Walks/Maps/Sugarloaf_Walk.html


## How to Use the Maps

1. **Accessing the Map**:
   - Open your web browser.
   - Type the URL or click on the provided link for the specific map you want to view.

2. **Interacting with the Map**:
   - *Zoom In/Out*: Use the zoom controls to focus on specific areas.
   - *Pan*: Click and drag to move around the map.
   - *Markers*: Click on markers to get more information about each location.
   - *Filter*: Click on layer symbol in top right corner, allowing you to toggle on or off the different coloured icons.

## Contributing to the Maps

If you would like to contribute to the maps, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/roryyarr/ASOC-Walks.git


### Explanation
1. **Table of Contents**: Provides an overview of the sections in the README.
2. **Overview**: Brief description of the project.
3. **Features**: Key features of the project.
4. **Requirements**: Necessary libraries and Python version.
5. **Setup**: Folder structure and instructions to install required libraries.
6. **Usage**: Steps to clone the repository, run the script, and view the map.
7. **Google Sheet Structure**: Example structure for the Google Sheet used in the project.
8. **Notes**: Additional notes about accessibility and configuration.
9. **License**: Licensing information.


### Running the Script

1. **Save the README**: Save the `README.md` file in the root of your repository.
2. **Push the Repository**:
   ```sh
   git add .
   git commit -m "Add README.md"
   git push origin main

## License
This project is licensed under the MIT License.

