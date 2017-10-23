from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

app.route('/')
def index():
    # "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game")) # redirect to /game

app.route('/game', methods=['GET', 'POST'])
def game_engine():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
    else:
        pass

if __name__ == "__main__":
    app.run()
