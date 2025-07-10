from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# Expanded Quotes with emojis
quotes = [
    "🔥 Stay hungry, stay foolish.",
    "💻 Talk is cheap. Show me the code.",
    "🧠 First, solve the problem. Then, write the code.",
    "🔍 Code never lies, comments sometimes do.",
    "🚀 Programs must be written for people to read, and only incidentally for machines to execute.",
    "🎯 Simplicity is the soul of efficiency.",
    "🐍 In case of fire: git commit, git push, leave building.",
    "🤖 Walking on water and developing software from a specification are easy if both are frozen.",
    "⚙️ Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "📖 Experience is the name everyone gives to their mistakes.",
    "🧩 Before software can be reusable it first has to be usable.",
    "📊 Code is like humor. When you have to explain it, it’s bad.",
    "🛡️ The best error message is the one that never shows up.",
    "🧪 Debugging is like being the detective in a crime movie where you are also the murderer.",
    "🎨 Make it work, make it right, make it fast."
]

# HTML template with a GIF and styled quote
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Random Quote</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            text-align: center;
            padding-top: 50px;
        }
        h2 {
            color: #333;
            font-size: 2rem;
            margin-top: 20px;
        }
        img {
            width: 300px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" alt="Coding GIF">
    <h2>{{ quote }}</h2>
</body>
</html>
"""

@app.route('/')
def get_quote():
    quote = random.choice(quotes)
    # if client requests JSON response
    if request.args.get('format') == 'json':
        return jsonify({"quote": quote})
    return render_template_string(html_template, quote=quote)

@app.route('/health')
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
