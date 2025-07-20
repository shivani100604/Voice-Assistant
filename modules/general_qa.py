import os
import wikipedia
import google.generativeai as genai

# Google Gemini API Key (free)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


def answer_general_question(query):
    # First try Google Gemini
    if GEMINI_API_KEY:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(query)
            answer = response.text.strip()
            if answer and not answer.lower().startswith("sorry"):
                return f"{answer}"
        except Exception as e:
            print("Gemini error:", e)

    # Fallback: Wikipedia
    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"{summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            summary = wikipedia.summary(e.options[0], sentences=2)
            return f"{summary}"
        except:
            return "I couldn't find a clear answer on Wikipedia."
    except:
        return "I couldn't find any answer."

