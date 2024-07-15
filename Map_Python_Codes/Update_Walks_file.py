import folium
import pandas as pd

# Google Sheets URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1mGR_xugxcg3Pc3e1KLzggZn6XfnSJOuHncZ64hOo8M4/export?format=csv'

# Read the data into a DataFrame
df = pd.read_csv(sheet_url)
df

# Extract data from the DataFrame
names = df['Name'].tolist()
locations = df[['Latitude', 'Longitude']].values.tolist()
links = df['Link'].tolist()
addresses = df['Address'].tolist()
descriptions = df['Description'].tolist()
routes = df['Routes'].tolist()

# Create a map centered around the first location
m = folium.Map(location=(-32.9, 151.79), zoom_start=10)

# Add markers for each location
for name, loc, link, address, desc, route in zip(names, locations, links, addresses, descriptions, routes):
    folium.Marker(
        location=loc,
        popup=f"<b>{name}</b><br><a href='{link}' target='_blank'>Google Maps Link</a><br>{address}<br>{desc}<br><a href='{route}' target='_blank'>Route Map Link</a>",
        tooltip=name
    ).add_to(m)

# Save the map as an HTML file
html_file = '/ASOC_walk_locations_map.html'
m.save(html_file)

print(f"Map has been saved to {html_file}")