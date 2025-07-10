from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# Coding Quotes
quotes = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Code never lies, comments sometimes do.",
    "Programs must be written for people to read, and only incidentally for machines to execute.",
    "Simplicity is the soul of efficiency.",
    "In case of fire: git commit, git push, leave building.",
    "Walking on water and developing software from a specification are easy if both are frozen.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "Experience is the name everyone gives to their mistakes.",
    "Before software can be reusable it first has to be usable.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "The best error message is the one that never shows up.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "Make it work, make it right, make it fast."
]

# Emojis
emojis = ["🔥", "💻", "🧠", "🔍", "🚀", "🎯", "🐍", "🤖", "⚙️", "📖", "🧩", "📊", "🛡️", "🧪", "🎨", "😎", "🤯", "🎉", "🦾", "📚"]

# Emotional Intelligence Messages
eq_quotes = [
    "🧘 Stay calm — not every battle is worth fighting.",
    "💡 Self-awareness is the foundation of emotional intelligence.",
    "🤝 Empathy isn’t weakness — it’s strength.",
    "🛑 Pause before you react, respond with intention.",
    "🎯 Know your triggers, manage your emotions.",
    "✨ Celebrate small wins, they matter too.",
    "📖 Listen to understand, not to reply.",
    "💪 Vulnerability builds genuine connection.",
    "🚪 It's okay to walk away from negativity.",
    "🌱 Growth starts where comfort ends."
]

# GIF URLs
gifs = [
    "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
    "https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif",
    "https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif",
    "https://media.giphy.com/media/fAnEC88LccN7a/giphy.gif",
    "https://media.giphy.com/media/26u4cqiYI30juCOGY/giphy.gif",
    "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif",
    "https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif",
    "https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif",
    "https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif",
    "https://media.giphy.com/media/l2SpPLRY0MNi53zqI/giphy.gif",
    "https://media.giphy.com/media/kDcfy1jSr9M6k/giphy.gif",
    "https://media.giphy.com/media/Y4pAQv58ETJgRwoLxj/giphy.gif",
    "https://media.giphy.com/media/3o6nURkRnx5rOUgv20/giphy.gif",
    "https://media.giphy.com/media/xUPGcjGy8I928yIlAQ/giphy.gif",
    "https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif",
    "https://media.giphy.com/media/l3vQX0FjSfT3uZ3iY/giphy.gif",
    "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
    "https://media.giphy.com/media/TilmLMmWrRYYHjLfub/giphy.gif",
    "https://media.giphy.com/media/d31vTpVi1LAcDvdm/giphy.gif",
    "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"
]


# HTML Template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Dev & EQ Daily Boost</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef2f3;
            text-align: center;
            padding-top: 50px;
        }
        h2, h3 {
            margin: 20px auto;
        }
        h2 {
            font-size: 2rem;
            color: #222;
        }
        h3 {
            font-size: 1.2rem;
            color: #555;
        }
        img {
            width: 300px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <img src="{{ gif_url }}" alt="Random Dev GIF">
    <h2>{{ emoji }} {{ quote }}</h2>
    <h3>{{ eq_quote }}</h3>
</body>
</html>
"""

@app.route('/')
def get_quote():
    quote = random.choice(quotes)
    emoji = random.choice(emojis)
    eq_quote = random.choice(eq_quotes)
    gif_url = random.choice(gifs)

    if request.args.get('format') == 'json':
        return jsonify({
            "emoji": emoji,
            "quote": quote,
            "emotional_intelligence": eq_quote,
            "gif_url": gif_url
        })

    return render_template_string(html_template, quote=quote, emoji=emoji, eq_quote=eq_quote, gif_url=gif_url)

@app.route('/health')
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
