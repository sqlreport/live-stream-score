from flask import Flask, render_template
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    remainingTimeWhenStopped = int(localStorage.getItem("remainingTimeWhenStopped"))
    minutes = Math.floor(remainingTimeWhenStopped / 60000)
    seconds = Math.floor((remainingTimeWhenStopped % 60000) / 1000)
    milliseconds = Math.floor(remainingTimeWhenStopped % 1000 / 100)
    time = minutes + ":" + seconds.toString().padStart(2, "0") + "." + milliseconds
    return render_template('score.html', time=time)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
