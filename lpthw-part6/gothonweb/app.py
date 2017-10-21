from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

app.route('/')
def index():
    greeting = "Start game"
    return render_template("index.html", greeting=greeting)

app.route('/game')
def game_engine():
    pass

if __name__ == "__main__":
    app.run()
