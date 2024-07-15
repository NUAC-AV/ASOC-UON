import folium
import gpxpy

"""
Code asks user input to create the 
Returns:

None
"""
while True:
    gpx_file = input("gpx file name")
    output_file = input("What would you like to name the file?")

    # Prompt user for marker details
    print("Enter marker details:")
    name = input("Name: ")
    link = input("Link: ")
    icon = input("Icon: ").strip().lower()
    colour = input("Colour: ")
    description = input("Description: ")

    # Ask the user if they want to add change names
    proceed = input("Do you want to move on? (y/n): ").strip().lower()
    if proceed == 'y':
        break



# Open the GPX file
with open(gpx_file, 'r') as f:
    gpx = gpxpy.parse(f)

# Extract coordinates from the GPX file
route = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            route.append((point.latitude, point.longitude))


# Loop allows users to change settings
while True:
    while True:
        centre = int(input("Which node do you want to be the centre? (int)" ))
        if centre > len(route):
            print("The route only has ",len(route),"points. Please choose a smaller number.")
            continue
        else:
            break
    zoom = int(input("What zoom setting do you want? (int)"))
        


    # Create a map centered around the specified point
    if route:
        start_point = route[centre]
    else:
        start_point = [0, 0]

    # Initialize map layer
    m = folium.Map(location=start_point, zoom_start=zoom)
    
    # Add the GPX route to the map
    folium.PolyLine(route, color='blue', weight=2.5, opacity=1).add_to(m)

    # Check if the icon is the ASOC logo and inalize the logo
    if icon == 'asoc':
        custom_icon = folium.CustomIcon(custom_icon_path, icon_size=(50, 50))
    else:
        custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')


    # Add start marker to the map
    folium.Marker(
        location=route[0],
        popup=f"<b>{name}</b><br><a href='{link}' target='_blank'>Google Maps Link</a><br>{description}",
        tooltip=name,
        icon=custom_icon
    ).add_to(m)



    # Ask user if they want a endpoint marker
    flag = input("Do you want to make a end marker? (y/n)").strip().lower()
    if flag == 'y':
        # Prompt user for marker details
        print("Enter marker details:")
        name = input("Name: ")
        icon = input("Icon: ")
        colour = input("Colour: ")
        description = input("Description: ")

        # Make endpoint marker Icon
        custom_icon = folium.Icon(color=colour, icon=icon, prefix='fa')

        # Add endpoint marker to the map
        folium.Marker(
            location=route[-1],
            popup=f"<b>{name}</b><br>{description}",
            tooltip=name,
            icon=custom_icon
        ).add_to(m)

    # Ask the user if they want to add change names
    proceed = input("Do you want to move on? (y/n): ").strip().lower()
    if proceed == 'y':
        break



# Save the map as an HTML file
m.save(output_file)
print(f"Map has been saved to {output_file}")
