from street_map_converter import StreetMapConverter

places = ["Birmingham Gardens, Newcastle, Australia",
          "Shortland, Newcastle, Australia",
          "Jesmond, Newcastle, Australia",
          "North Lambton, Newcastle, Australia",
          ]

output_directory = "Letterbox_Maps/GeoJSON"
filename = "MAP3.geojson"

converter = StreetMapConverter(places)
converter.process(output_directory=output_directory, filename=filename)