from flask import Flask

faisalapp = Flask(__name__)

@faisalapp.route('/')
def home():
    return "Hello from Faisal Flask app!"
