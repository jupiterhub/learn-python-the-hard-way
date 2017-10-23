from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

app.route('/')
def index():
    greeting = "Start game"
    return render_template("index.html", greeting=greeting)

app.route('/game')
def game_engine():
    return render_template("game.html")

if __name__ == "__main__":
    app.run()
