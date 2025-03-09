from flask import Flask, request, jsonify
import ollama
from flask_cors import CORS
  

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_input = data["message"]

    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_input}])
        bot_response = response['message']['content']
        return jsonify({"response": bot_response})  

    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render uses port 10000
