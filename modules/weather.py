import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city="Delhi"):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return "Weather API key is missing."

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            return "Couldn't fetch the weather."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f" The weather in {city} is {weather} with a temperature of {temp}°C."

    except Exception as e:
        print("Weather Error:", e)
        return "Couldn't fetch the weather."
