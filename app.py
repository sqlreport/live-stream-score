from flask import Flask, render_template, request
import os 
import redis

app = Flask(__name__)
redis_url = os.environ.get('REDIS_URL')
redis_db = redis.from_url(redis_url, decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score/<string:game_id>')
def score(game_id):
    return render_template('score.html', game_id=game_id)

@app.route('/match')
def match():
    return render_template('match.html')

@app.route('/match/<string:game_id>/time', methods=['GET','POST'])
def remaining_time(game_id):
    if request.method == 'POST':
        
        if request.is_json:
            data = request.get_json()
            remaining_time = data.get('remainingTimeWhenStopped')
            # you can use the game_id and remaining_time values as needed
            # store the data in a database, update an existing record, etc.
            redis_db.set(game_id, remaining_time)
            print('Remaining time for game ID {} is {}'.format(game_id, remaining_time))
            return jsonify({'remaining_time': remaining_time})
        else:
            print('No remaining time found for game ID {}'.format(game_id))
            return jsonify({'remaining_time': 0})
    
        
    else:
        remaining_time = redis_db.get(game_id)
        if remaining_time:
            print('Remaining time for game ID {} is {}'.format(game_id, remaining_time))
            return jsonify({'remaining_time': remaining_time})
        else:
            print('No remaining time found for game ID {}'.format(game_id))
            return jsonify({'remaining_time': 0})
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
