// Add a message to the chatbox
function addMessage(sender, message) {
    const chatbox = document.getElementById("chatbox");
    const msgDiv = document.createElement("div");
    msgDiv.className = "message " + (sender === "user" ? "user-msg" : "bot-msg");
    msgDiv.textContent = (sender === "user" ? "🙋 " : "💬 ") + message;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Send message to backend
function sendMessage() {
    const input = document.getElementById("userInput");
    const userMessage = input.value.trim();
    if (!userMessage) return;

    addMessage("user", userMessage);
    input.value = "";

    fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        addMessage("bot", data.response);
        speakText(data.response); // Speak the response
    })
    .catch(error => console.error("Error:", error));
}

// Text-to-Speech (Voice output)
function speakText(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-IN";
    window.speechSynthesis.speak(speech);
}

// Speech-to-Text (Mic input)
function startListening() {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Your browser does not support voice recognition!");
        return;
    }

    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";
    recognition.start();

    recognition.onresult = function(event) {
        const userVoice = event.results[0][0].transcript;
        document.getElementById("userInput").value = userVoice;
        sendMessage();
    };

    recognition.onerror = function(event) {
        console.error("Voice recognition error:", event.error);
    };
}

// Event listeners
document.getElementById("sendBtn").addEventListener("click", sendMessage);
document.getElementById("micBtn").addEventListener("click", startListening);
document.getElementById("userInput").addEventListener("keypress", function (e) {
    if (e.key === "Enter") sendMessage();
});
