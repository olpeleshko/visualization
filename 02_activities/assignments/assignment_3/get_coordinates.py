import csv
import requests


# This script reads Parking Occupancy dataset retrieved from https://open.toronto.ca/dataset/parking-occupancy/
# and compliments it with latitude and longitude data (based on Car Park Location column) retrieved from OpenstreetMap
# Ensure that the Parking Occupancy.csv file is located in 02_activities/assignments/assignment_3 folder
# The output file will be called Parking Occupancy With Coordinates.csv and will be created in the same directory.
new_rows = []
with open("./02_activities/assignments/assignment_3/Parking Occupancy.csv") as f:
    reader = csv.reader(f)
    cols = next(reader)
    print(cols)
    for row in reader:
        address = f"{row[2]}, Toronto, Ontario, Canada"
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
        response = requests.get(url, headers={'User-Agent': 'geo-sample'})
        data = response.json()

        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            new_row = row + [lat, lon]
            new_rows.append(new_row)

with open("./02_activities/assignments/assignment_3/Parking Occupancy With Coordinates.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows([cols + ["Latitude", "Longitude"]] + new_rows)