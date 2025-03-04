import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded
if not OPENAI_API_KEY:
    raise ValueError("❌ API Key is missing! Make sure it's in the .env file.")

# Initialize OpenAI client correctly
openai.api_key = OPENAI_API_KEY

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        
        # Generate response from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Compatible model
            messages=[{"role": "user", "content": user_input}],
            max_tokens=100
        )
        
        bot_response = response.choices[0].message["content"].strip()

    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
