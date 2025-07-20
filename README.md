# Voice Assistant Web App

A Flask-based **Voice Assistant** that can answer questions, fetch weather updates, display news, and provide general knowledge using **Wikipedia** and free APIs.

## Features
- Weather updates (for any city).
- Latest news headlines.
- General question answering using Wikipedia.
- Fun facts feature.
- Voice input (using browser mic).
- Interactive chat UI with a send button and mic button.
- Free AI fallback to Wikipedia answers.

## Project Structure
voice-assistant/
├── app.py               
├── assistant.py          
├── modules/             
│   ├── general_qa.py
│   ├── news.py
│   ├── weather.py
│   └── facts.py
├── static/               
│   ├── style.css
│   ├── script.js
│   └── logo.png
├── templates/
│   └── index.html        
├── requirements.txt     
└── README.md             

## Installation and Setup
1. Clone the Repository
   git clone https://github.com/shivani100604/Voice-Assistant.git
   cd Voice-Assistant

2. Install dependencies
   pip install -r requirements.txt

3. Add API keys in .env file
   WEATHER_API_KEY=your_openweather_api_key
   NEWSDATA_API_KEY=your_newsdata_api_key
   GEMINI_API_KEY=your_gemini_api_key

5. Run the app
   python app.py

Then open http://127.0.0.1:5000/ in your browser.
