import os
import requests
from dotenv import load_dotenv

# Load environment variables (only needed locally, not in Render)
load_dotenv()

# Get API key from environment
NEWS_API_KEY = os.getenv("NEWS_API_KEY") or os.getenv("NEWSDATA_API_KEY")

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
        response = requests.get(url, params=params, timeout=8)
        if response.status_code != 200:
            return "📰 Couldn't fetch the news. Try again later."

        data = response.json()
        articles = data.get("results", [])

        if not articles:
            return "📰 No news found."

        headlines = [f"• {article.get('title', 'No title')}" for article in articles[:3]]
        return "📰 News:\n" + "\n".join(headlines)

    except Exception as e:
        print("News fetch error:", e)
        return "📰 Couldn't fetch the news."
