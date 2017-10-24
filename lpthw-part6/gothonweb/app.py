from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

@app.route('/')
def index():
    # "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game")) # redirect to whichever url was in game()

@app.route('/game', methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # in case the user access /game directly
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            print("ACTION:",action)
            print("NEXT ROOM:", next_room)

            if not next_room:
                # repeat same room
                session['room_name'] = planisphere.name_room(room)
            else:
                # move to next room
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))

# CHANGE THIS IF TOU PUT IN THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?R'

if __name__ == "__main__":
    app.run()
