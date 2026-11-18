import requests

def get_weather(location):
    try:
        # latitude and longitude
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": location, "count": 1}
        ).json()
        
        if "results" not in geo:
            print("Location not found!")
            return
            
        place = geo["results"][0]

       # get the weather
    weather = requests.get(https://api.open-meteo.com/v1/forecast",
                           params={
                               "latitude": place["latitude"],
                               "longitude": place["longitude"],
                               "current" : "temperature_2m,weather_code"
                               "timezone": "auto"

                           }).json()
                           temperature = weather["current"][temperature_2m]
                           code = weather["current"]["weather_code"] 
                           # weather code into condition
                           weather_conditions = {

                           }

                           condition = weather_conditions.get(code, "Unknown")
                           print(f"Location: {place['name']}")
                           print(f"Location: {place['name']}")
    except Exception as e:
        print(f"Error finding location: {e}")
        return

if __name__ == "__main__":
    location = input("Enter a location to get the latitude and longitude: ")
    get_weather(location)
