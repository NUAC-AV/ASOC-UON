# Interactive Map from Google Sheets

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install Required Libraries](#install-required-libraries)
- [Running Code](# )
- [Usage](#usage)
  - [Clone the Repository](#clone-the-repository)
  - [Run the Script](#run-the-script)
  - [View the Map](#view-the-map)
- [Google Sheet Structure](#google-sheet-structure)
  - [Example Google Sheet](#example-google-sheet)
- [Notes](#notes)
- [License](#license)

## Overview
This project provides a Python scripts to read data from a ASOC_Walks_Database Google Sheets document. Which is used to create an interactive map with markers using the `folium` library. The map is saved as an HTML file, which can be viewed in any web browser.

https://docs.google.com/spreadsheets/d/1mGR_xugxcg3Pc3e1KLzggZn6XfnSJOuHncZ64hOo8M4/edit?fbclid=IwZXh0bgNhZW0CMTAAAR3rcnaz2qedGxf1LaI0fz7X7gUQiZrvZTjs3x-MfPTNZODKO8ykz3piWDI_aem_mtzQRofiQxsPinF7C6uSHg&gid=0#gid=0

## Features
- Read data from "ASOC_Walks_Database"
- Create an interactive map from the database
- Add markers for each location with popups containing relevant information
- Save the map as an HTML file

## Requirements
- Python 3.x
- `pandas` library
- `folium` library
- `gpxpy` libary

## Setup

### Install Required Libraries
Make sure you have `pandas` and `folium` installed. You can install these libraries using `pip`:

```sh
pip install folium
pip install pandas
pip install gpxpy

## Usage
You can access any of the maps by the link https://roryyarr.github.io/ASOC-Walks/filename.
For example https://roryyarr.github.io/ASOC-Walks/strava_route_map.html or 
