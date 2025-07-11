import datetime
from modules.general_qa import answer_general_question
from modules.weather import get_weather
from modules.news import get_latest_news
from modules.facts import get_random_fact

def process_query(query):
    query = query.lower().strip()
    response = ""

     # Greetings
    if any(phrase in query for phrase in ["how are you", "how r u", "hello", "hi", "hey"]):
        response = "Hello! I'm doing great. How can I help you today?"

    # Time
    elif "time" in query:
        now = datetime.datetime.now()
        response = f"⏰ The current time is {now.strftime('%I:%M %p')}."

    # Date
    elif "date" in query:
        today = datetime.date.today()
        response = f"📅 Today's date is {today.strftime('%B %d, %Y')}."

    # Weather
    elif "weather" in query:
        response = get_weather(query)

    # News
    elif "news" in query:
        response = get_latest_news()

    # Facts
    elif "fact" in query or "tell me a fact" in query:
        response = "🧠 Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!"

    # Fallback to General QnA
    else:
        response = answer_general_question(query)

    return response
