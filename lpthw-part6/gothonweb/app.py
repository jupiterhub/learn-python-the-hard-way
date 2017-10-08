# ex50.py, simple web server
# server supports hot reload
from flask import Flask # web framework/server
from flask import render_template # loads templates using jinja2
from flask import url_for # Identify URL
# interpreter sets default values for __name__
# think of Thread name.
# this is "__main__"
# if you run the module it will be the module name
app = Flask(__name__)

# index mappings
@app.route('/')
def index():
    greeting = "Hello World"
    # looks at templates/ (variables for 2nd argument)
    return render_template("index.html", greeting=greeting)

# dynamic parameter
@app.route('/greet/<message>')
def greet(message):
    return render_template("index.html", greeting=message)

# with is try-finally block. we call it on Flasks built in method
with app.test_request_context():
    # use url_for when generating urls
    print(url_for('index'))
    print(url_for('greet', message="hello"))

# only run the server if
# running directly (not an import)
if __name__ == "__main__":
    app.run()
