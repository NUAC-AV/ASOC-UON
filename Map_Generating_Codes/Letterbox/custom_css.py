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
            width: 350px;     /* Increase width of the control */
        }
        .leaflet-control-layers-toggle {
            width: 50px;  /* Adjust the toggle button width */
            height: 50px; /* Adjust the toggle button height */
            background-size: 80px 80px; /* Adjust background icon size */
            background-image: url('Images/ASOC-Logo-orange.png');  /* Use your custom image */
            background-repeat: no-repeat;
            background-position: center;
        }
        .leaflet-control-layers-overlays label {
            font-size: 18px;  /* Increase font size of labels */
            padding: 5px 10px;  /* Add padding to labels */
        }
        /* Increase the size of checkboxes */
        input[type="checkbox"] {
            width: 20px;
            height: 20px;
            transform: scale(1.5); /* Adjust the scale factor as needed */
            transform-origin: top left;
            transform: scale(1.5); /* Adjust the scale factor as needed */
            transform-origin: top left;
            margin-right: 15px; /* Add space between the checkbox and text */
            margin-top: 4px;    /* Add a small margin above the checkbox */
            margin-bottom: 4px; /* Add a small margin below the checkbox */
        }
        </style>
        """
        self.map.get_root().html.add_child(Element(custom_css))
