import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Weather condition ASCII art
WEATHER_ART = {
    "clear": """
       ☀️
    Clear Sky
    """,
    "clouds": """
       ☁️ ☁️
    Cloudy
    """,
    "rain": """
       ☁️
      💧💧💧
    Rainy
    """,
    "snow": """
       ☁️
      ❄️❄️❄️
    Snowy
    """,
    "default": """
       🌤️
    Weather
    """
}

def get_weather(city, units="metric"):
    api_key = os.getenv("API_KEY")  # Load API key from environment variable
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units={units}"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            
            temp = main["temp"]
            feels_like = main["feels_like"]
            humidity = main["humidity"]
            description = weather["description"].lower()
            
            # Determine weather icon
            if "clear" in description:
                icon = WEATHER_ART["clear"]
            elif "cloud" in description:
                icon = WEATHER_ART["clouds"]
            elif "rain" in description:
                icon = WEATHER_ART["rain"]
            elif "snow" in description:
                icon = WEATHER_ART["snow"]
            else:
                icon = WEATHER_ART["default"]
                
            return {
                "temp": temp,
                "feels_like": feels_like,
                "humidity": humidity,
                "description": description,
                "icon": icon
            }
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None