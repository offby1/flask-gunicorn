# Run me with
#         FLASK_APP=hello.py pipenv run flask run
# or
#         pipenv run gunicorn hello:app

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
