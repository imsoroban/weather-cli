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
        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": "temperature_2m,weather_code",
                "timezone": "auto"
            }
        ).json()
        
        temperature = weather["current"]["temperature_2m"]
        code = weather["current"]["weather_code"] 
        
        # weather code into condition
        weather_conditions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            95: "Thunderstorm"
        }

        condition = weather_conditions.get(code, "Unknown")
        print(f"Location: {place['name']}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather Condition: {condition}")
        
    except Exception as e:
        print(f"Error finding location: {e}")
        return

if __name__ == "__main__":
    location = input("Enter a location to get the latitude and longitude: ")
    get_weather(location)