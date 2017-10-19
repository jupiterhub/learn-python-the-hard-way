from flask import Flask
from flask import render_template

app = Flask(__name__)

app.route('/')
def index():
    pass

app.route('/game')
def game_engine():
    pass

if __name__ == "__main__":
    app.run()
