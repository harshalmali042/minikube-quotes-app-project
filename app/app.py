from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Code never lies, comments sometimes do."
]

@app.route('/')
def get_quote():
    return f"<h2>{random.choice(quotes)}</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
