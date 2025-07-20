import requests
import os

NEWS_API_KEY = os.getenv("NEWSDATA_API_KEY")

def get_latest_news(country="in"):
    if not NEWS_API_KEY:
        return "News API key is missing."

    url = f"https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&country={country}&language=en&category=top"

    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if res.status_code != 200 or "results" not in data:
            return "Couldn't fetch the news."

        articles = data["results"][:3]
        headlines = [f"• {a['title']}" for a in articles]
        return "Latest News:\n" + "\n".join(headlines)

    except Exception as e:
        print("News fetch error:", e)
        return "Couldn't fetch the news."
