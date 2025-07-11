# LG Voice Guard

A smart and beautiful voice assistant web app built with **Flask, JavaScript, and Gemini AI**. It can answer general questions, tell the weather, provide news, control devices (mocked), and interact via voice in a chatbox-style UI.

---

## ✨ Features

* Ask general knowledge questions
* Weather updates by city
* Latest news headlines
* Smart chatbox UI with speech recognition
* Responds via text and voice (text-to-speech)
* Gemini + Wikipedia fallback for accurate answers

---

## 🚀 Live Demo

You can deploy it for free using **Render** or run it locally.

---

## 🎓 Technologies Used

* Python + Flask
* HTML + CSS + JS
* Google Gemini API (Free tier)
* OpenWeather API (for weather)
* NewsData API (for news)
* Speech Recognition (JS)
* pyttsx3 (TTS)

---

## 📁 Folder Structure

```
voice-assistant/
├── app.py
├── assistant.py
├── modules/
│   ├── weather.py
│   ├── news.py
│   ├── general.py
│   └── speak.py
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── image.png
├── templates/
│   └── index.html
├── .env
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### Step 1: Clone the repo

```bash
git clone https://github.com/yourusername/voice-assistant
cd voice-assistant
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Add `.env` file

Create a `.env` file in the root folder and add:

```
GEMINI_API_KEY=your_gemini_key_here
WEATHER_API_KEY=your_openweather_key_here
NEWS_API_KEY=your_newsdata_key_here
```

### Step 4: Run the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🌐 Deploy on Render

1. Push project to GitHub
2. Go to [https://render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repo
5. Set:

   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `python app.py`
6. Add Environment Variables:

   * `GEMINI_API_KEY`
   * `WEATHER_API_KEY`
   * `NEWS_API_KEY`
7. Deploy and open your URL

---

## 👥 Author

**Shivani**
Email: [sgangwar592@gmail.com](mailto:sgangwar592@gmail.com)
GitHub: [shivani100604](https://github.com/shivani100604)

---

## 🗓️ License

This project is free to use and modify.
