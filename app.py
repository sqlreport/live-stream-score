from flask import Flask, render_template
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/match')
def match():
    return render_template('match.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
