from flask import Flask, request, jsonify
from translate import translate
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def health_check():
    """Confirms service is running"""
    return "Machine translation English to French service is up and running."

@app.route('/translate1', methods=["POST"])
def get_prediction1():
    text = request.json['text']
    translation = translate(text)
    return jsonify({"output":translation})

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)