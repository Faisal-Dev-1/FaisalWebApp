from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Faisal! Flask with Gunicorn on Linux is running.</h1>"
