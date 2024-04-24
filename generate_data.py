import csv
import requests

VESSELS_URL = 'http://localhost:8000/api/vessels/'


with open('data-fs-exercise.csv') as data_file:
    reader = csv.reader(data_file, delimiter=',')

    data = []

    for row in reader:
        data.append({
            'vessel_id': row[0],
            'position_time': row[1],
            'latitude': row[2],
            'longitude': row[3]
        })

    for position in data:
        response = requests.post(VESSELS_URL, data=position)
        if response.status_code != 201:
            print(f'Vessel ID #{position.get("vessel_id")} Error: {response.json()}')

