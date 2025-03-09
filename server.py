from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route('/chat', methods=['POST'])  # Ensure this route exists
def chat():
    data = request.json
    user_message = data.get("message", "")

    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_message}])
    
    return jsonify({"response": response["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
