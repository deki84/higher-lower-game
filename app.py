from flask import Flask, render_template
import random
from game_data import data 
from art import logo, vs 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-game')
def run_game():
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    result = f"{account_a['name']} ({account_a['follower_count']} Follower) vs {account_b['name']} ({account_b['follower_count']} Follower)"

    return result

if __name__ == "__main__":
    app.run(debug=True)
