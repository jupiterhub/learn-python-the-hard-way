all the static files (CSS/JS/etc.) from Flask are looked up here.

To generate URL use the following:

'static' is a special endpoint name
url_for('static', filename='style.css')
