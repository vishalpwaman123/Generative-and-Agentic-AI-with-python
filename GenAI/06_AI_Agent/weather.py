import requests

API_KEY = "2fa47fd8f8ba7b94b3b8b0cd4c8e6a54"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_by_city(city: str) -> dict:
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=5)

        # Raise error for bad status codes (4xx, 5xx)
        response.raise_for_status()

        data = response.json()

        # Validate API response
        if data.get("cod") != 200:
            return {"error": data.get("message", "Unknown error")}

        # Format clean response
        weather_info = {
            # "city": data.get("name"),
            # "country": data.get("sys", {}).get("country"),
            "temperature": data.get("main", {}).get("temp"),
            "feels_like": data.get("main", {}).get("feels_like"),
            "humidity": data.get("main", {}).get("humidity"),
            "weather": data.get("weather", [{}])[0].get("description"),
            "wind_speed": data.get("wind", {}).get("speed")
        }
    
        return weather_info
    
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

# API Response 
# {
#     'coord': {'lon': 73.8553, 'lat': 18.5196}, 
#     'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
#     'base': 'stations', 
#     'main': {'temp': 30.99, 'feels_like': 29.63, 'temp_min': 30.99, 'temp_max': 30.99, 'pressure': 1011, 'humidity': 29, 'sea_level': 1011, 'grnd_level': 939}, 
#     'visibility': 10000, 
#     'wind': {'speed': 4.35, 'deg': 279, 'gust': 5.58}, 
#     'clouds': {'all': 0}, 'dt': 1775371078, 
#     'sys': {'country': 'IN', 'sunrise': 1775350538, 'sunset': 1775395124}, 
#     'timezone': 19800, 
#     'id': 1259229, 
#     'name': 'Pune', 
#     'cod': 200
# }

print(get_weather_by_city("pune"))