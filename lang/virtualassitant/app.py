from flask import Flask, request, jsonify

# Importing functions from the assistant module
from assistant import answer_question, summarize_document, get_weather

app = Flask(__name__)

# Default route for homepage
@app.route('/')
def home():
    return "<h1>Welcome to the Virtual Assistant API!</h1><p>Use the available endpoints: /question, /summarize, /weather.</p>"

# Route to answer questions
@app.route('/question', methods=['POST'])
def question():
    data = request.json
    question = data.get("question", "")
    answer = answer_question(question)
    return jsonify({"answer": answer})

# Route to summarize a document
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    document = data.get("document", "")
    summary = summarize_document(document)
    return jsonify({"summary": summary})

# Route to fetch weather information
@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get("city", "Unknown")
    weather_info = get_weather(city)
    return jsonify({"weather": weather_info})

# Route to handle favicon.ico requests (optional)
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Returns a no-content response for favicon.ico requests

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
