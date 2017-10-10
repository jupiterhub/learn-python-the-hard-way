# ex50.py, simple web server
# server supports hot reload
from flask import Flask # web framework/server
from flask import render_template # loads templates using jinja2
from flask import url_for # Identify URL
from flask import request # for HTTP Methods
from flask import redirect # for redirecting requets

# For file upload
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "C:\\2-dev\\PythonProjects\\learn-python-the-hard-way\\lpthw-part6\\gothonweb\\files"
ALLOWED_EXTENSIONS = ['png','jpg', 'jpeg', 'gif']
# interpreter sets default values for __name__
# think of Thread name.  this is "__main__"
# run inside an imported module and it will be the module name
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
      return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# index mappings
@app.route('/')
def index():
    # get request parameter
    name = request.args.get('name', 'Nobody')

    if name:
        greeting= f"Hello {name}"
    else:
        # won't be reached there's always a fallback
        greeting = "Hello World"

    # looks at templates/ (variables for 2nd argument)
    return render_template("index.html", greeting=greeting)

# ex51
@app.route("/hello", methods=['POST', 'GET', 'UPDATE'])
def hello():
    greeting = "Hello World"

    if request.method == "UPDATE":
        return render_template("hello_form_laid_out.html")
    elif request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"

        # ~~~~~~~~~~~~~~~~~~~~~ file
        if 'file' in request.files:
            uploaded_file = request.files['file']

            if uploaded_file.filename == '':
                print('No selected file')
                return redirect(request.url)
            if uploaded_file and allowed_file(uploaded_file.filename):
                # encrypt, so hacker cant use ../../../touch hacked.txt
                filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template("index_laid_out.html", greeting=greeting)
    else:
        return render_template("hello_form_laid_out.html")


# dynamic parameter
@app.route('/greet/<message>', methods=['GET', 'POST'])
def greet(message):
    if (request.method == 'GET'):
        return render_template("index.html", greeting=message)
    else:
        pass

# with is try-finally block. we call it on Flasks built in method
with app.test_request_context():
    # use url_for when generating urls
    print(url_for('index'))
    print(url_for('greet', message="hello"))
    print("Request method is:", request.method)

# only run the server if
# running directly (not an import)
if __name__ == "__main__":
    app.run()
