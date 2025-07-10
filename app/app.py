from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Code never lies, comments sometimes do."
]

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
            padding-top: 100px;
        }
        h2 {
            color: #333;
            font-size: 2rem;
        }
    </style>
</head>
<body>
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
