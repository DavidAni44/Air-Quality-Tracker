from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv('API_KEY')

def getLocation():
    location = []
    LOCATION_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?"
    CITY = "Manchester"

    url = LOCATION_BASE_URL + "q=" + CITY + "&limit="+ "1" + "&appid=" + API_KEY

    responses = requests.get(url).json()

    lat = responses[0]["lat"]
    lon = responses[0]["lon"] 

    location.append(lat)
    location.append(lon)
    
    return location


def getAirQuality():
    AQ_BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution?"
    aq_location = getLocation()
    
    lat = aq_location[0]
    lon = aq_location[1]
    
    aq_url = AQ_BASE_URL + "lat=" + str(lat) + "&lon="+ str(lon) + "&appid=" + API_KEY
    
    responses = requests.get(aq_url).json()
    
    aqi = responses["list"][0]["main"]["aqi"]
    
    return aqi


print(getAirQuality())
    
    


