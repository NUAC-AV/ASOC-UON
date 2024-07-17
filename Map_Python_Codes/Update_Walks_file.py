import folium
import pandas as pd

# Google Sheets URL
sheet_url = "https://docs.google.com/spreadsheets/d/1mGR_xugxcg3Pc3e1KLzggZn6XfnSJOuHncZ64hOo8M4/export?format=csv&gid=0"

# Read the data into a DataFrame
df = pd.read_csv(sheet_url)

# Gets varibles from google sheets
names = df['Name'].tolist()
locations = df[['Latitude', 'Longitude']].values.tolist()
links = df['Google_Link'].tolist()
routes = df['Route_Link'].tolist()
addresses = df['Address'].tolist()
descriptions = df['Description'].tolist()
icons = df['Icon'].tolist()
colours = df['Colour'].tolist()

# Create a map centered around the newcastle region
m = folium.Map(location=(-32.9, 151.79), zoom_start=11)

# Create a dictionary to hold feature groups based on color
feature_groups = {}

# Add markers for each location
for name, loc, link, route, address, desc, icon, colour in zip(names, locations, links, routes, addresses, descriptions, icons, colours):
    # Set a default icon if the icon field is blank
    if pd.isna(icon) or icon == "":
        icon = 'info-sign'  # Default icon

    # Replaces NaN with empty strings
    desc = "" if pd.isna(desc) else desc
    #route = "" if pd.isna(route) else route
    len = "" if pd.isna(len) else len

    # Defines point icon
    if icon == 'asoc':
            custom_icon_path = "Pictures/ASOC-Logo-orange.png"
            custom_icon = folium.CustomIcon(custom_icon_path, icon_size=(70, 32))
        else:
            custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')

    # Adds link as either google map pin of route map if it exists in the google sheets. 
    if pd.isna(route):
        marker_link = f"<a href='{link}' target='_blank'>Google Map Link</a><br>"
    else:
        marker_link = f"<a href='{route}' target='_blank'>Route Map Link</a><br>"

    # Create a feature group for the colour if it doesn't exist
    if colour not in feature_groups:
        feature_groups[colour] = folium.FeatureGroup(name=colour)

    # Adds marker for the point to the feature group based on colour
    folium.Marker(
        location=loc,
        popup = f"<b>{name}</b><br>{marker_link}{desc}<br>",
        tooltip=name,
        icon = custom_icon
    ).add_to(feature_groups[colour])

# Add all feature groups to the map
for fg in feature_groups.values():
    fg.add_to(m)

# Add layer control to toggle different layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
html_file = 'Maps/ASOC_walk_locations_map.html'
m.save(html_file)

print(f"Map has been saved to {html_file}")