from flask import Flask, render_template, request, jsonify
from assistant import process_query

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"response": "Please ask something!"})
    response = process_query(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    print("Voice Assistant Backend Running!")
    app.run(host="0.0.0.0", port=5000, debug=True)
