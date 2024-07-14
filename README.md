# Interactive Map from Google Sheets

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install Required Libraries](#install-required-libraries)
- [Usage](#usage)
  - [Clone the Repository](#clone-the-repository)
  - [Run the Script](#run-the-script)
  - [View the Map](#view-the-map)
- [Google Sheet Structure](#google-sheet-structure)
  - [Example Google Sheet](#example-google-sheet)
- [Notes](#notes)
- [License](#license)

## Overview
This project provides a Python script to read data from a Google Sheets document and create an interactive map with markers using the `folium` library. The map is saved as an HTML file, which can be viewed in any web browser.

## Features
- Read data from a publicly accessible Google Sheet
- Create an interactive map centered around the first location
- Add markers for each location with popups containing relevant information
- Save the map as an HTML file

## Requirements
- Python 3.x
- `pandas` library
- `folium` library

## Setup

### Install Required Libraries
Make sure you have `pandas` and `folium` installed. You can install these libraries using `pip`:

```sh
pip install pandas folium
