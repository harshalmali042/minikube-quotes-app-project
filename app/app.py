from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# 30 Developer Quotes
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
    "Make it work, make it right, make it fast.",
    "A user interface is like a joke. If you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "Deleted code is debugged code.",
    "Programmers are tools for converting caffeine into code.",
    "Weeks of coding can save you hours of planning.",
    "The best code is no code at all.",
    "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
    "Documentation is like sex: when it’s good, it’s very good; when it’s bad, it’s better than nothing.",
    "Never trust a computer you can’t throw out a window.",
    "Programming without an extremely heavy use of console.log is like being blind.",
    "Software is like entropy: It is difficult to grasp, weighs nothing, and obeys the Second Law of Thermodynamics.",
    "Software undergoes beta testing shortly before it’s released. Beta is Latin for 'still doesn’t work.'",
    "Computers are fast; developers keep it slow.",
    "It's not a bug – it’s an undocumented feature.",
    "The code you write makes you a programmer. The code you delete makes you a good one."
]

# Emojis
emojis = ["🔥", "💻", "🧠", "🔍", "🚀", "🎯", "🐍", "🤖", "⚙️", "📖", "🧩", "📊", "🛡️", "🧪", "🎨", "😎", "🤯", "🎉", "🦾", "📚"]

# Emotional Intelligence quotes
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

# 20 Developer GIF URLs
gif_urls = [
    "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
    "https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif",
    "https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif",
    "https://media.giphy.com/media/fAnEC88LccN7a/giphy.gif",
    "https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif",
    "https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif",
    "https://media.giphy.com/media/Y4pAQv58ETJgRwoLxj/giphy.gif",
    "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif",
    "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
    "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
    "https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif",
    "https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif",
    "https://media.giphy.com/media/kDcfy1jSr9M6k/giphy.gif",
    "https://media.giphy.com/media/5xtDarqCp0eomZaFJWc/giphy.gif",
    "https://media.giphy.com/media/TilmLMmWrRYYHjLfub/giphy.gif",
    "https://media.giphy.com/media/l2SpPLRY0MNi53zqI/giphy.gif",
    "https://media.giphy.com/media/xUPGcjGy8I928yIlAQ/giphy.gif",
    "https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif",
    "https://media.giphy.com/media/l3vQX0FjSfT3uZ3iY/giphy.gif",
    "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif"
]

# Shuffle GIFs for initial random order
random.shuffle(gif_urls)
gif_index = 0

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Developer Wisdom & EQ Daily</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            text-align: center;
            padding-top: 50px;
        }
        h2, h3 {
            color: #333;
            margin: 20px auto;
        }
        h2 {
            font-size: 2rem;
        }
        h3 {
            font-size: 1.3rem;
            color: #666;
        }
        img {
            width: 320px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <img src="{{ gif_url }}" alt="Coding GIF">
    <h2>{{ emoji }} {{ quote }}</h2>
    <h3>{{ eq_quote }}</h3>
</body>
</html>
"""

@app.route('/')
def get_quote():
    global gif_index

    quote = random.choice(quotes)
    emoji = random.choice(emojis)
    eq_quote = random.choice(eq_quotes)
    gif_url = gif_urls[gif_index]

    gif_index += 1
    if gif_index >= len(gif_urls):
        random.shuffle(gif_urls)
        gif_index = 0

    if request.args.get('format') == 'json':
        return {
            "emoji": emoji,
            "quote": quote,
            "emotional_intelligence": eq_quote,
            "gif_url": gif_url
        }

    return render_template_string(html_template, quote=quote, emoji=emoji, eq_quote=eq_quote, gif_url=gif_url)

@app.route('/health')
def health_check():
    return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
