# Description: This file is used to get the data from the RoomAnalyser API and print it out.

import requests
import json
from datetime import datetime

# Din API-nøgle fra OpenWeatherMap
api_key = "2f445d2f64db28369a09a5d4149a8be7a8b8e59a47ffdfa3dbc02820ab14d3df"
lane = "sensor_list"
account = 442
time = datetime.now()
print(time) 
# url https://app.roomalyzer.com/index.php?w2d=mould&api_key=2f445d2f64db&room=bedroom&temperature=20&humidity=50

base_url = f"https://app.roomalyzer.com/api/index.php?api_key={api_key}&account={account}&time={time}&lane={lane}"

response = requests.get(base_url)
print(response)
data = response.json()
print(data[0])