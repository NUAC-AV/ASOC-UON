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


### Folder Structure
- **Church_Locations**: Contains location data.
- **GPX_Routes**: Contains GPX route files.
- **Map_Python_Codes**: Contains Python files for mapping.
  - **Update_Walks_file.py**: Updates the ASOC_walk_locations_map.html file with the current Google Sheets data.
  - **Create_Routes_map.py**: Creates a map for a route.
  - **Create_Route_UI.py**: Script for creating routes with a user interface.
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

## Google Sheet Structure
- **Name**: The name of the location.
- **Latitude**: The latitude of the location.
- **Longitude**: The longitude of the location.
- **Link**: A Google Maps link or other relevant URL.
- **Address**: The address of the location.
- **Description**: A description of the location or any additional notes.
- **Icon****: The icon to use for the marker.
- **Colour**: The color of the marker.

## License
This project is licensed under the MIT License.

### MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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

