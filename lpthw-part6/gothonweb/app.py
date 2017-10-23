from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

app.route('/')
def index():
    # "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game")) # redirect to /game

app.route('/game')
def game_engine():
    return render_template("game.html")

if __name__ == "__main__":
    app.run()
