import datetime
import re
from modules.weather import get_weather
from modules.news import get_latest_news
from modules.general_qa import answer_general_question
from modules.facts import get_random_fact

def extract_city(query):
    """
    Extracts a possible city name from queries like 'weather of Bareilly'.
    """
    match = re.search(r"weather\s+(?:in|of)\s+([a-zA-Z\s]+)", query)
    return match.group(1).strip() if match else None

def process_query(query):
    query = query.lower().strip()
    response = ""

    # Time
    if "time" in query:
        now = datetime.datetime.now()
        response = f"The current time is {now.strftime('%I:%M %p')}."

    # Date
    elif "date" in query:
        today = datetime.date.today()
        response = f"Today's date is {today.strftime('%B %d, %Y')}."

    # Weather
    elif "weather" in query:
        city = extract_city(query)
        if city:
         response = get_weather(city)
        else:
         response = "Please specify a city, e.g., 'weather of Delhi'."

         response = "Please specify a city, e.g., 'weather of Delhi'."

    # News
    elif "news" in query:
        response = get_latest_news()

    # Facts
    elif "fact" in query or "tell me a fact" in query:
        response = f"Did you know? {get_random_fact()}"
        
     # Greetings
    elif any(word in query for word in ["how are you", "hello", "hi", "hey"]):
        response = "Hello! I'm doing great. How can I help you today?"

    # General Q&A
    else:
        response = answer_general_question(query)

    return response
