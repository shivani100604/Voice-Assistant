import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="Delhi"):
    if not WEATHER_API_KEY:
        return "⚠️ Weather API key is missing."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200 or data.get("cod") != 200:
            return "💬 Couldn't fetch the weather."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city.lower()} is {weather} with a temperature of {temp}°C."
    except Exception as e:
        print("Weather error:", e)
        return "💬 Couldn't fetch the weather due to an error."
