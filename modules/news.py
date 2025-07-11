import os
import requests

NEWS_API_KEY = os.getenv("NEWSDATA_API_KEY")  # Use this exact name in Render

def get_latest_news(country="in", category="top"):
    if not NEWS_API_KEY:
        return "⚠️ News API key is missing."

    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWS_API_KEY,
        "country": country,
        "language": "en",
        "category": category
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200 or not data.get("results"):
            return "📰 No news found."

        articles = data["results"][:3]
        headlines = [f"• {article['title']}" for article in articles]
        return "📰 News:\n" + "\n".join(headlines)

    except Exception as e:
        print("News fetch error:", e)
        return "📰 Couldn't fetch the news."
