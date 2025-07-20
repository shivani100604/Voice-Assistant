import requests
import os

OPENWEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    if not OPENWEATHER_API_KEY:
        return "Weather API key is missing."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if res.status_code != 200 or "main" not in data:
            return f"Couldn't fetch the weather for {city}."

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        return f"The weather in {city.title()} is {weather} with {temp}°C."

    except Exception as e:
        print("Weather fetch error:", e)
        return f"Couldn't fetch the weather for {city}."
