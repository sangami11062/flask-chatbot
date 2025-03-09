from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # Allows frontend access

@app.route('/chat', methods=['POST'])  # Ensure this route exists
def chat():
    try:
        data = request.json
        print("Received Data:", data)  # Debugging print
        user_message = data.get("message", "")

        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_message}])
        print("Ollama Response:", response)  # Debugging print
        
        return jsonify({"response": response["message"]["content"]})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500  # Return error message

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)  # Ensure Flask listens on all interfaces
