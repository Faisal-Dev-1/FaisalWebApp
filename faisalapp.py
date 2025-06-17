from flask import Flask

faisalapp = Flask(__name__)

@faisalapp.route('/')
def home():
    return "Hello from Faisal Flask app!"

if __name__ == '__main__':
    faisalapp.run()
