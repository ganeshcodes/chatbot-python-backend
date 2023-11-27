from flask import Flask, request, jsonify
from flask_cors import CORS
import time
app = Flask(__name__)
# Add origin restriction for production deployment
CORS(app)

# Respond to user prompt
@app.route('/chat', methods=['POST'])
def chat():
    # delay added to test loading icon on chatbot-barebone-react-app
    time.sleep(1)
    prompt = request.json.get('prompt', '')
    # Decide what to do with the prompt (eg., RAG/LangChain/GPT to answer the prompt)
    response = f"Received: {prompt}"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)