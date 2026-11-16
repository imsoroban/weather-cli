import requests

def get_weather(location):
    try:
        #latitude and longitude
geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",[cite: 1]
                  params={"name": location, "count": 1}).json()[cite: 1]
        if "results" not in geo:
            print("Location not found!")
            return

            