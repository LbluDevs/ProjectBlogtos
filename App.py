import imp
from flask import Flask
from flask import render_template, url_for, redirect



app = Flask(__name__)


@app.route("/")
def loginPage():
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)