# LG Voice Guard

**LG Voice Guard** is an intelligent voice assistant built using Python and Flask. It can answer general knowledge questions, fetch weather updates, get news, respond to smart commands, and interact through speech and a web-based chat interface. All answers are spoken aloud and displayed in a beautiful chat UI.

![Logo](static/logo.png)

---

## Features

- 🎙️ Voice input via microphone
- 💬 Chat-style text interface
- 🌦️ Get real-time weather updates
- 📰 Read latest news headlines
- 📚 Answer general knowledge questions (uses Google Gemini & Wikipedia)
- 💡 Respond to smart phrases like "turn on light", "off the fan"
- 📢 Speaks responses using text-to-speech
- 💻 Works in browser using Flask web app

---

## Folder Structure

```
voice-assistant/
├── app.py                  # Flask app
├── assistant.py            # Main assistant logic
├── speak.py                # Text-to-speech script
├── modules/
│   ├── general_qa.py       # Handles general questions
│   ├── weather.py          # Weather info using OpenWeatherMap
│   ├── news.py             # News headlines using NewsAPI
│   └── facts.py            # Fun facts
├── templates/
│   └── index.html          # Main webpage UI
├── static/
│   ├── css/
│   │   └── style.css       # Styling
│   ├── js/
│   │   └── script.js       # Speech recognition + chatbot logic
│   ├── logo.png            # Logo for the project
│   └── image.png           # Chatbox UI screenshot
├── requirements.txt        # Python libraries
└── README.md               # This file
```

---

##  Requirements

Install Python libraries:

```bash
pip install flask pyttsx3 requests wikipedia google-generativeai python-dotenv
```

---

## How to Run

1. Clone the repository or download it as ZIP and extract.
2. Make sure all files are in place.
3. Create a `.env` file in root directory and add:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key
   ```
4. Run the app:

```bash
python app.py
```

5. Open browser and go to:

```
http://127.0.0.1:5000
```

---

##  Screenshot

![Chat UI](static/image.png)

## 🙋 How it Works

- Press the 🎙️ mic button to speak
- Assistant listens and shows your message
- Answers using Gemini API or Wikipedia
- Responds with voice and text

---

## 👩‍💻 Author

**Shivani Gangwar**  
Email: sgangwar592@gmail.com  
GitHub: [shivani100604](https://github.com/shivani100604)
