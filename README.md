<a id="readme-top"></a>
# ASOC UON


<!-- TABLE OF CONTENTS -->
<details>
  <summary>📚 Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-structure">Project Structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#viewing-maps">Viewing Maps</a>
      <ul>
        <li><a href="#example-maps">Example Maps</a></li>
        <li><a href="#how-to-use">How To Use</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li>
      <a href="#requirements">Requirements</a>
      <ul> 
        <li><a href="#installing-libraries">Installing Libraries</a></li>
      </ul>
    </li>
    <li>
      <a href="#setup">Setup</a>
      <ul>
        <li><a href="#google-sheet-structure">Google Sheet Structure</a></li>
        <li><a href="#example-google-sheet">Example Google Sheet</a></li>
        <li><a href="#map-icon-symbols">Map Icon Symbols</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#updating-sabbath-walks-map">Updating Sabbath Walks Map</a></li>
        <li><a href="#creating-route-map">Creating Route Map</a></li>
        <li><a href="#updating-letterbox-map">Updating Letterbox Map</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing To The Maps</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

    


<!-- About the Project -->
## About The Project
This project provides Python scripts to create interactive HTML maps, which can be viewed in any web browser.
Specifically, maps are created for ASOC church locations/routes, Sabbath walks and letterboxing.

### Project Structure
- **GPX_Files**: Contains all GPX files
  - *[Church_Locations](GPX_Files/Church_Locations/)*: Contains GPX files for Church Locations.
  - *[Letterbox_Routes](GPX_Files/Letterbox_Routes/)*: Contains GPX files of completed Letterbox routes.
  - *[Misc](GPX_Files/Misc/)*: Contains any other gpx files
  - *[Sabbath_Walks](GPX_Files/Sabbath_Walks)*: Contains GPX files for Sabbath walks.
  - *[GPX_Studio.md](GPX_Files/GPX_Studio.md)*: Details how to produce GPX file using GPX Studio.
- **Map_Generating_Codes**: Contains the code for generating maps.
  - *[Create_Routes](Map_Generating_Codes/Create_Routes/)*: Creates a route.
  - *[Letterbox](Map_Generating_Codes/Letterbox/)*: Creates the letterbox maps.
  - *[Misc](Map_Generating_Codes/Misc/)*: Other codes.
  - *[Route_Code](Map_Generating_Codes/Route_Code/)*
  - *[README.md](Map_Generating_Codes/README.md/)*
  - *[Update_Walks.py](Map_Generating_Codes/Update_Walks.py/)*: Updates the map of ASOC walks
- **Maps**: Contains the HTML files for the maps.
  - *[Church_Locations](Maps/Church_Locations/)*: Contains maps for church and caregroup locations.
  - *[Letterbox](Maps/Letterbo/)*: Contains maps used for letterboxing.
  - *[Misc](Maps/Misc/)*: Other maps.
  - *[Sabbath_Walks](Maps/Sabbath_Walks/)*: Contains maps for Sabbath walks.
- **Images**: Contains all images used in this repo.
  - *[Icons](Images/Icons/)*: Contains Font Arewsome Icons 
- **ASOC_Walks.ipynb**: Jupyter notebook for code testing.
- **CHANGELOG.md**: Records changes between versions.
- **LICENSE**: Explains the licensing of this project.
- **README.md**: Explains this project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Viewing Maps
The maps can be viewed through GitHub Pages. You can access them using the following link format:
https://roryyarr.github.io/ASOC-Walks/`file-name`.html

Replace `file-name` with the specific file you want to view. 
Note: replace spaces(" ") with "%20". 

### Example Maps

Here are some example usages of the maps:

1. **Main ASOC Walk Locations Map**:
   - **Description**: This map shows the main locations for the ASOC walks.
   - **Link**: https://nuac-av.github.io/ASOC-UON/Maps/Misc/ASOC_walk_locations_map.html

2. **Mount Sugarloaf Map**:
   - **Description**: This map highlights the route for the mount Sugarloaf walk.
   - **Link**:  https://nuac-av.github.io/ASOC-UON/Maps/Sabbath_Walks/Mount%20Sugarloaf/Sugarloaf_Walk.html


### How To Use

1. **Accessing the Map**:
   - Open your web browser.
   - Type the URL or click on the provided link for the specific map you want to view.

2. **Interacting with the Map**:
   - *Zoom In/Out*: Use the zoom controls to focus on specific areas.
   - *Pan*: Click and drag to move around the map.
   - *Markers*: Click on markers to get more information about each location.
   - *Filter*: Click on layer symbol in top right corner, allowing you to toggle on or off the different coloured icons.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Features
- Creates Interactive Sabbath Walk Maps:
  - Using the following sheet as a backend: [Google Sheets Document](https://docs.google.com/spreadsheets/d/1mGR_xugxcg3Pc3e1KLzggZn6XfnSJOuHncZ64hOo8M4/edit?fbclid=IwZXh0bgNhZW0CMTAAAR3rcnaz2qedGxf1LaI0fz7X7gUQiZrvZTjs3x-MfPTNZODKO8ykz3piWDI_aem_mtzQRofiQxsPinF7C6uSHg&gid=0#gid=0)
  - Reads data from the google sheets.
  - Plots 
- Create an interactive map from the database
- Add markers for each location with popups containing relevant information
- Save the map as an HTML file
- Add GPX routes from a folder and group them on the same level as regions in the tree structure

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Requirements
- Python 3.x
- `numpy` library
- `pandas` library
- `geopandas` libary
- `folium` library
- `gpxpy` library
- `pdf2image` library
- `Pillow` library
- `OSMnx` library
- `shapely` library

### Installing Libraries
Make sure you have the libraries installed. You can install these libraries using `pip install library-name`
<details>
  <summary>📚 Commands for downloading libraries</summary>
  <ol>
    <ol>
      <pre><code>pip install numpy</code></pre>
    </ol>
    <ol>
      <pre><code>pip install pandas</code></pre>
    </ol>
    <ol>
      <pre><code>pip install geopandas</code></pre>
    </ol>
    <ol>
      <pre><code>pip install folium</code></pre>
    </ol>
    <ol>
      <pre><code>pip install gpxpy</code></pre>
    </ol>
    <ol>
      <pre><code>pip install pdf2image</code></pre>
    </ol>
    <ol>
      <pre><code>pip install pillow</code></pre>
    </ol>
    <ol>
      <pre><code>pip install osmnx</code></pre>
    </ol>
    <ol>
      <pre><code>pip install shapely</code></pre>
    </ol>
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Setup -->
## Setup

The Sabbath Walk, Caregroup and Church locations are stored in a google sheet. With the following structure.

### Google Sheet Structure
- **Name**: The name of the location.
- **Latitude**: The latitude of the location.
- **Longitude**: The longitude of the location.
- **Google_Link**: A Google Maps link or other relevant URL.
- **Address**: The address of the location.
- **Description**: A description of the location or any additional notes.
- **Route_Link**: A link to the route map for that location.
- **Icon**: The icon to use for the marker.
- **Colour**: The colour of the marker.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Example Google Sheet
| Location | Latitude | Longitude | Google_Link | Address | Discription | Route_Link  | Icon | Color |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|Awabakal Nature Reserve  | -32.99149503 | 151.7222826  | [Link](https://www.google.com/maps/place/13+Ivy+St,+Dudley+NSW+2290/data=!4m6!3m5!1s0x6b7317ca43cdc65d:0x6eedd6577b803386!7e2!8m2!3d-32.9917425!4d151.7222826?utm_source=mstt_1&entry=gps&lucs=,47075915&g_ep=CAESCjExLjEwOS4xMDEYACDXggMqCSw0NzA3NTkxNUICQVU%3D)   | 13 Ivy St, Dudley NSW 2290      | It will be in the bush, so please have proper walking shoes for the walk. We can park on the road around Ivy Street. | [Link](https://nuac-av.github.io/ASOC-UON/Maps/Sabbath_Walks/Mount%20Sugarloaf/Sugarloaf_Walk.html) | tree  | green |
| Bar Beach  | -32.94047053 | 151.7695674  | [Link](https://www.google.com/maps/place/Yuelarbah+Track,+Bar+Beach+NSW+2300/@-32.9406461,151.764718,946m/data=!3m2!1e3!4b1!4m15!1m8!3m7!1s0x6b73143fbd4c9111:0x5017d681632e890!2sBar+Beach+NSW+2300!3b1!8m2!3d-32.9377866!4d151.7701917!16s%2Fm%2F02x66br!3m5!1s0x6b73143e338a20c5:0xbac9ffd0659c571a!8m2!3d-32.9406507!4d151.7695889!16s%2Fg%2F11m_lcwt1h?entry=ttu) | Yuelarbah Track, Bar Beach NSW 2300 |  |  | umbrella-beach | beige |
| ⋮  | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮  | ⋮  |



### Map Icon Symbols

| Icon Symbol                                             | Icon Name        | Colour                                           | Description                   |
|:-------------------------------------------------------:|:----------------:|:------------------------------------------------:|:-------------------------------------------------:|
| ![water icon](Images/Icons/water.svg)                   | `water`          | <span style="color:blue">blue</span>             | Used for rivers and lakes (excluding saltwater).  |
| ![plant-wilt icon](Images/Icons/plant-wilt.svg)         | `plant-wilt`     | <span style="color:lightgreen">lightgreen</span> | Used for wetlands.                     |
| ![tree icon](Images/Icons/tree.svg)                     | `tree`           | <span style="color:green">green</span>           | Used for forests and parks.                        |
| ![umbrella-beach icon](Images/Icons/umbrella-beach.svg) | `umbrella-beach` | <span style="color:beige">beige</span>           | For beaches and other sandy environments.           |
| ![mountain icon](Images/Icons/mountain.svg)             | `mountain`       | <span style="color:darkgreen">darkgreen</span>   | For hilly and mountainous walks.            |
| ![sailboat icon](Images/Icons/sailboat.svg)             | `sailboat`       | <span style="color:pink">pink</span>             | For boat ramps.                        |
| ![ferry icon](Images/Icons/ferry.svg), ![ship icon](Images/Icons/ship.svg) | `Ferry` and `Ship` | <span style="color:black">black</span> | Used for other harbour/coastal walks.  |
| ![flag icon](Images/Icons/flag.svg)                     | `flag`           | <span style="color:red">red</span>               | Other walks not listed.                       |

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Icon Colors and Symbols
The available colors for icons are: `black`, `beige`, `lightblue`, `gray`, `blue`, `darkred`, `lightgreen`, `purple`, `red`, `green`, `lightred`, `white`, `darkblue`, `darkpurple`, `cadetblue`, `orange`, `pink`, `lightgray`, `darkgreen`.

More details can be found [here](https://www.kaggle.com/code/aungdev/colors-available-for-marker-icons-in-folium).

Icons can be chosen from [Font Awesome](https://fontawesome.com/search?o=r&m=free). Additionally, PNG files can be used as icons.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

clone the repo, then exacute the following codes.
```shh
git clone https://github.com/NUAC-AV/ASOC-UON.git
```

### Updating Sabbath Walks Map

<ol>
  <li> 
    <details>
      <summary>Pull latest GitHub repository</summary>
      <pre><code>git pull origin</code></pre>
    </details>
  </li>
  <li> Ensure the Google Sheets is correctly formatted. </li>
  <li> Run the Update_Walks.py file. </li>
  <li>
    <details>
      <summary>Commit changes</summary>
      <pre><code>git commit -m "Update Sabbath Walks Map."</code></pre>
    </details>
  </li>
  <li>
    <details>
      <summary>Push changes to the remote repo</summary>
      <pre><code>git push origin main</code></pre>
    </details>
  </li>
</ol>



### Creating Route Map

To be updated.
1. 
2. 
3. 


### Updating Letterbox Map
 
<ol>
  <li>
    <details>
      <summary>Pull latest:</summary>
      <pre><code>git pull origin</code></pre>
    </details>
  </li>
  <li>
    Add all gpx files to GPX_Files/Letterbox_Routes folder.
  </li>
  <li>
    Run Update_Letterbox_Map.py file.
  </li>
  <li>
    <details>
      <summary>Track gpx files:</summary>
      <pre><code>git add .</code></pre>
    </details>
  </li>
  <li>
    <details>
      <summary>Commit changes:</summary>
      <pre><code>git commit -m "📮 Update letterbox map</code></pre>
    </details>
  </li>
  <li>
    <details>
      <summary>Push changes:</summary>
      <pre><code>git push origin main</code></pre>
    </details>
  </li> 
</ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add route maps for all walks
- [ ] Redesign create_route_map codes

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contributing To The Maps

If you would like to contribute to the maps, follow these steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/name-of-changes`)
3. Commit your Changes (`git commit -m 'Add name-of-changes'`)
4. Push to the Branch (`git push origin feature/name-of-changes`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact
`Rory Yarr`
- **Email**: roryyarrcoder@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/rory-yarr-3a5833211/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments
- **OSMnx**: Boeing, G. 2017. "OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks." Computers, Environment and Urban Systems, 65, 126-139. https://doi.org/10.1016/j.compenvurbsys.2017.05.004


