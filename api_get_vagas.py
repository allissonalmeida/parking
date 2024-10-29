import requests
import json

# Load data files json
data = requests.get("http://sistemas.doissinspection.com/api/parking_lot.json")
data = data.json()

# Write data to a JSON file
with open('parking_lot.json', 'w') as f:
    json.dump(data, f)

#print(data['1']['vagas_livre'])
#print(data['2']['vagas_livre'])