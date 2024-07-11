"""
This module implements a Flask web application that serves a home page
and an emotion detection endpoint.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Renders the home page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """Handles POST requests to the emotion detection endpoint."""
    data = request.json
    text_to_analyze = data.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again."}), 400

    response_text = (
        f"Para la frase dada, la respuesta del sistema es 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"y 'sadness': {result['sadness']}. La emoción dominante es {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
