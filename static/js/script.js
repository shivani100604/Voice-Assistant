let recognizing = false;
const recognition = new webkitSpeechRecognition();
recognition.continuous = false;
recognition.lang = 'en-US';

function toggleListening() {
    if (!recognizing) {
        recognition.start();
        recognizing = true;
    } else {
        recognition.stop();
        recognizing = false;
    }
}

recognition.onresult = function(event) {
    const text = event.results[0][0].transcript;
    addMessage('user', "🙋 " + text);
    fetch('/process', {
        method: 'POST',
        body: JSON.stringify({ query: text }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(res => res.json())
    .then(data => {
        addMessage('bot', "💬 " + data.response);

        const utterance = new SpeechSynthesisUtterance(data.response);
        window.speechSynthesis.speak(utterance);
    });
};

function addMessage(sender, text) {
    const box = document.getElementById("chatbox");
    const msg = document.createElement("div");
    msg.className = sender;
    msg.textContent = text;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}
