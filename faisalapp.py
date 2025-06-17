from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Faisal! Flask on Azure Linux Web App with Gunicorn.</h1>"
