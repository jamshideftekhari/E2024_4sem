import requests

# Din API-nøgle fra Climatiq
api_key = "B3QRB3TC6X4CVEW82JZN44682R"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# URL til API'en
url = "https://api.climatiq.io/data/v1/estimate"

# Oplysninger om transport og distance
data = {
    "emission_factor": {"activity_id": "passenger_vehicle-vehicle_type_car-fuel_source_na-distance_na-engine_size_na",
                        "data_version": "^6"},
    "parameters": {
        "distance": 100,
        "distance_unit": "km"
    }
}

# Send forespørgsel
response = requests.post(url, headers=headers, json=data)

# Tjek og vis resultat
if response.status_code == 200:
    result = response.json()
    print("CO2-udledning:", result["co2e"], result["co2e_unit"])
else:
    print("Fejl ved forespørgsel:", response.status_code, response.text)
