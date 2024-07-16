import folium
import pandas as pd

# Google Sheets URL


sheet_url = "https://docs.google.com/spreadsheets/d/1mGR_xugxcg3Pc3e1KLzggZn6XfnSJOuHncZ64hOo8M4/export?format=csv&gid=0"

# Read the data into a DataFrame
df = pd.read_csv(sheet_url)
df


names = df['Name'].tolist()
locations = df[['Latitude', 'Longitude']].values.tolist()
links = df['Google_Link'].tolist()
routes = df['Route_Link'].tolist()
addresses = df['Address'].tolist()
descriptions = df['Description'].tolist()
lengths = df['Length']
icons = df['Icon'].tolist()
colours = df['Colour'].tolist()

# Create a map centered around the first location
m = folium.Map(location=(-32.9, 151.79), zoom_start=11)

# Add markers for each location
for name, loc, link, route, address, desc, len, icon, colour in zip(names, locations, links, routes, addresses, descriptions, lengths, icons, colours):
    # Set a default icon if the icon field is blank
    if pd.isna(icon) or icon == "":
        icon = 'info-sign'  # Default icon

    # Replaces NaN with empty strings
    desc = "" if pd.isna(desc) else desc
    #route = "" if pd.isna(route) else route
    len = "" if pd.isna(len) else len

    custom_icon = folium.Icon(color = colour, icon=icon, prefix='fa')

    route_link = f"<a href='{route}' target='_blank'>Route Map Link</a><br>" if not pd.isna(route) else ""

    folium.Marker(
        location=loc,
        popup = f"<b>{name}</b><br>{route_link}{desc}<br>",
        tooltip=name,
        icon = custom_icon
    ).add_to(m)

# Save the map as an HTML file
html_file = 'Maps/ASOC_walk_locations_map.html'
m.save(html_file)

print(f"Map has been saved to {html_file}")