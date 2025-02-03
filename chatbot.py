import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up your OpenAI API key
OPENAI_API_KEY = "your-api-key-here"

def get_chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful customer service assistant."},
                  {"role": "user", "content": user_input}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"].strip()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
