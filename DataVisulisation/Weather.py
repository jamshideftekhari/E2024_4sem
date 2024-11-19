import requests

# Din API-nøgle fra OpenWeatherMap
api_key = "f7df200f9ede8d6ae7a92b525668362d"
# Byen, du vil hente vejrudsigten for
city = "Copenhagen"
# URL til API'en med by og nøgle
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    # Send forespørgslen til OpenWeatherMap API
    response = requests.get(base_url)
    # Konverter svar til JSON-format
    data = response.json()

    # Tjek om forespørgslen var succesfuld
    if data["cod"] == 200:
        # Hent specifikke vejroplysninger
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        # Udskriv vejroplysninger
        print(f"Vejr i {city}:")
        print(f"Temperatur: {temperature}°C")
        print(f"Luftfugtighed: {humidity}%")
        print(f"Beskrivelse: {description.capitalize()}")
    else:
        print("Kunne ikke finde vejroplysninger for byen.")

except Exception as e:
    print("Fejl:", e)
