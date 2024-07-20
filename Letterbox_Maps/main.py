from street_map_converter import StreetMapConverter
"""
places = ["Birmingham Gardens, Newcastle, Australia",
          "Shortland, Newcastle, Australia",
          "Jesmond, Newcastle, Australia",
          "North Lambton, Newcastle, Australia",
          ""]
"""

Newcastle = [
    "Birmingham Gardens, Newcastle, Australia",
    "Shortland, Newcastle, Australia",
    "Jesmond, Newcastle, Australia",
    "Adamstown, Newcastle, Australia",
    "Bar Beach, Newcastle, Australia",
    "Broadmeadow, Newcastle, Australia",
    "Carrington, Newcastle, Australia",
    "Cooks Hill, Newcastle, Australia",
    "Hamilton, Newcastle, Australia",
    "Hamilton East, Newcastle, Australia",
    "Hamilton South, Newcastle, Australia",
    "Islington, Newcastle, Australia",
    "Kooragang, Newcastle, Australia",
    "Lambton, Newcastle, Australia",
    "Maryville, Newcastle, Australia",
    "Mayfield, Newcastle, Australia",
    "Mayfield East, Newcastle, Australia",
    "Mayfield West, Newcastle, Australia",
    "Merewether, Newcastle, Australia",
    "New Lambton, Newcastle, Australia",
    "Newcastle, Newcastle, Australia",
    "Newcastle East, Newcastle, Australia",
    "Newcastle West, Newcastle, Australia",
    "North Lambton, Newcastle, Australia",
    "Sandgate, Newcastle, Australia",
    "Stockton, Newcastle, Australia",
    "The Hill, Newcastle, Australia",
    "The Junction, Newcastle, Australia",
    "Tighes Hill, Newcastle, Australia",
    "Waratah, Newcastle, Australia",
    "Waratah West, Newcastle, Australia",
    "Wickham, Newcastle, Australia"
]

output_directory = "Letterbox_Maps/GeoJSON"


for suburb in Newcastle:
    filename = f{suburb}.geojson"

    converter = StreetMapConverter(places)
    converter.process(output_directory=output_directory, filename=filename)