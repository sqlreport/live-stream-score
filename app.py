from flask import Flask, render_template
import os 
import redis

app = Flask(__name__)
redis_db = redis.Redis(host=os.environ['REDIS_URL'], port=30044, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/match')
def match():
    return render_template('match.html')

@app.route('/match/<string:game_id>/time', methods=['GET','POST'])
def remaining_time(game_id):
    if request.method == 'POST':
        remaining_time = request.form.get('remaining_time')
        redis_db.set(game_id, remaining_time)
        return 'Remaining time for game ID {} set to {}'.format(game_id, remaining_time)
    else:
        remaining_time = redis_db.get(game_id)
        if remaining_time:
            return 'Remaining time for game ID {} is {}'.format(game_id, remaining_time.decode('utf-8'))
        else:
            return 'No remaining time found for game ID {}'.format(game_id)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
