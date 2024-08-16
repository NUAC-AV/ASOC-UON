# Creating GPX Files for a Route with GPX Studio

## 📚 Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Steps to Create GPX Files](#steps-to-create-gpx-files)
  - [Open GPX Studio](#open-gpx-studio)
  - [Create a New Route](#create-a-new-route)
  - [Draw Your Route](#draw-your-route)
  - [Edit the Route](#edit-the-route)
  - [Add Details](#add-details)
  - [Save and Export the Route](#save-and-export-the-route)
- [Saving and Sharing GPX Files](#saving-and-sharing-gpx-files)
- [Example GPX File](#example-gpx-file)
- [Additional Tips](#additional-tips)
- [References](#references)
- [License](#license)

## Overview
GPX (GPS Exchange Format) files are XML files that contain GPS data. They are commonly used to share routes, tracks, and waypoints. This guide will help you create GPX files for routes using GPX Studio.

## Requirements
- Basic knowledge of GPS and routes
- Access to an online tool like GPX Studio


## Steps to Create GPX Files

### Open GPX Studio
- Navigate to [GPX Studio](https://gpx.studio) in your web browser.

### Create a New Route
- Click on the "New Route" button to start planning your route.

### Draw Your Route
- Use the map interface to draw your route. Click on the map to set waypoints and create the route path. The waypoints will be connected automatically to form the route.

### Edit the Route
- Edit the waypoints by dragging them to new locations on the map. Add new waypoints by clicking on the map or remove existing waypoints by clicking on them and selecting the delete option.

### Add Details
- Add details such as route name, description, and additional information if needed.

### Save and Export the Route
- Once you are satisfied with your route, click on the "Save" button. Then, select "Export" and choose the "GPX" format to download the route as a GPX file.

## Naming the GPX File
When saving the GPX file, use the format `Route_Location_path_name.gpx` to clearly indicate the route and location details. For example, if you have a route from the library to the park, you could name the file `Library_Park_route.gpx`.

### Organize GPX Files into Subfolders
Save the GPX file into a subfolder within the `GPX_Routes` folder, named according to the location of the route. For example, for a route in Mount Sugarloaf, you might create a subfolder called `Mount_Sugarloaf` inside `GPX_Routes` and save the file there.

#### Example Folder Structure
GPX_Routes/
├── Basden_Theatre/
│ ├── Physics_Parking.gpx
├── Sydney/
│ ├── Science_Lane_Parking.gpx


## Saving and Sharing GPX Files
Once you have created a GPX file using GPX Studio, you can save it on your computer or share it with others. Here’s how:

1. **Save to Computer**: 
   - Save the GPX file to a specific location on your computer for easy access.
   - Rename 

2. **Share via Email**: 
   - Attach the GPX file to an email and send it to others.

3. **Upload to Cloud Storage**: 
   - Upload the GPX file to cloud storage services such as Google Drive, Dropbox, or OneDrive and share the link.

## Example GPX File
Below is an example of a simple GPX file structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="GPX Studio" xmlns="http://www.topografix.com/GPX/1/1">
  <trk>
    <name>Example Route</name>
    <trkseg>
      <trkpt lat="48.858844" lon="2.294351">
        <ele>35.0</ele>
        <time>2023-07-14T10:23:23Z</time>
      </trkpt>
      <trkpt lat="48.858844" lon="2.295051">
        <ele>36.0</ele>
        <time>2023-07-14T10:24:23Z</time>
      </trkpt>
    </trkseg>
  </trk>
</gpx>

