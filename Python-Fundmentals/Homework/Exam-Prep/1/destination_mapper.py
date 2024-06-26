import re

location_on_map = input()
regex = r"(\=|\/)([A-Z][a-zA-Z][a-zA-z]+)\1"
matches = re.findall(regex, location_on_map)

locations = []
travel_points = 0

for point in matches:
    travel_points += len(point[1])
for location in matches:
    locations.append(location[1])

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")
