import requests

def get_weather(location):
    try:
        #latitude and longitude
        geo = requests.get 