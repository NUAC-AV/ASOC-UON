from folium import Element

class CustomCSS:
    def __init__(self, map_object):
        self.map = map_object

    def add_css(self):
        custom_css = """
        <style>
        /* Increase the size of the layer control */
        .leaflet-control-layers {
            font-size: 16px;  /* Increase font size */
            padding: 10px;    /* Add padding around the control */
            width: 300px;     /* Increase width of the control */
        }
        .leaflet-control-layers-toggle {
            width: 40px;  /* Adjust the toggle button width */
            height: 40px; /* Adjust the toggle button height */
            background-size: 40px 40px; /* Adjust background icon size */
            background-image: url('Images/ASOC-Logo-orange.png');  /* Use your custom image */
            background-repeat: no-repeat;
            background-position: center;
        }
        .leaflet-control-layers-overlays label {
            font-size: 16px;  /* Increase font size of labels */
            padding: 5px 10px;  /* Add padding to labels */
        }
        </style>
        """
        self.map.get_root().html.add_child(Element(custom_css))
