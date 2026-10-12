# modules and global vars
from abc import ABC, abstractmethod
import requests

# abstract class
class WeatherAbstract(ABC):
        
    @abstractmethod
    def get_current_weather(self,lat,lon):
        pass


# open_weather class
class OpenWeatherProvider(WeatherAbstract):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key):
            self.api_key = api_key

    def get_current_weather(self,lat,lon):
        response = requests.get(self.base_url, params={
            "lat": lat,
            "lon": lon,
            "appid": self.api_key })
        normalize_data = {"temp": response.json()["main"]["temp"] - 273.1,
                          "humidity": response.json()["main"]["humidity"]}
        return normalize_data       
        

        
        
# openmeteo class
class OpenMeteoProvider(WeatherAbstract):
    base_url = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self,lat,lon):
        response = requests.get(self.base_url, params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m"})
    
        normalize_data = {"temp": response.json()["current"]["temperature_2m"],
                                  "humidity": response.json()["main"]["relative_humidity_2m"]}
        return normalize_data
        


# run the app
provider = OpenMeteoProvider()
provider = OpenWeatherProvider("c041f99bce87cd708668231e082cae46")
print(provider.get_current_weather(lat=34.640816, lon=50.89310774999999))