from flask import Flask

faisalapp = Flask(__name__)

@faisalapp.route("/")
def home():
    return "<h1>Hello Faisal! Flask on Azure Linux Web App with Gunicorn.</h1>"

if __name__ == "__main__":
    faisalapp.run(debug=True)   # **هنا يجب وجود مسافة بادئة**
