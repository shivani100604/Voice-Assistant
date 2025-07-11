import os
import wikipedia
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def answer_general_question(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat()
        response = chat.send_message(query)
        gemini_answer = response.text.strip()

        if gemini_answer.lower().startswith("sorry") or "couldn't answer" in gemini_answer.lower():
            raise ValueError("Weak Gemini response")

        return f"{gemini_answer}"

    except Exception as e:
        print("⚠️ Gemini failed:", e)

    # Try Wikipedia 
    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"{summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            summary = wikipedia.summary(e.options[0], sentences=2)
            return f"{summary}"
        except:
            pass
    except:
        pass

    return "❓ Sorry, I couldn't find an answer to that."
