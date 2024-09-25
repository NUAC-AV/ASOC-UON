from street_map_converter import StreetMapConverter

# Define the base list of newcastle suburbs
base_places = [
    "Birmingham Gardens",
    "Shortland",
    "Jesmond",
    "Adamstown",
    "Bar Beach",
    "Broadmeadow",
    "Carrington",
    "Cooks Hill",
    "Georgetown",
    "Hamilton",
    "Hamilton East",
    "Hamilton South",
    "Hamilton North"
    "Islington",
    "Kooragang",
    "Lambton",
    "Maryville",
    "Mayfield",
    "Mayfield East",
    "Mayfield West",
    "Merewether",
    "New Lambton",
    "Newcastle",
    "Newcastle East",
    "Newcastle West",
    "North Lambton",
    "Sandgate",
    "Stockton",
    "The Hill",
    "The Junction",
    "Tighes Hill",
    "Waratah",
    "Waratah West",
    "Wickham"
]

base_places = ["Birmingham Gardens",
    "Shortland",
    "Jesmond",
    "North Lambton",
    "Waratah West",
    "Waratah",
    "Georgetown",
    "Hamilton North"]


# Add the suffix to each place
places = [f"{place}, Newcastle, Australia" for place in base_places]


output_directory = "Letterbox_Maps/GeoJSON/Zone_1"


# Create geojsons
for base_place, suburb in zip(base_places, places):
    filename = f"{base_place.replace(' ', '_')}.geojson"  # Replace spaces with underscores for valid filenames

    converter = StreetMapConverter([suburb])
    converter.process(output_directory=output_directory, filename=filename)
    print(f"Processed and saved: {filename}")