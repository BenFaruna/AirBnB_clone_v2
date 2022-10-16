#!/usr/bin/python3
"""routing flask and displaying text"""
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """index page that prints message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route that displays a message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """rounting using dynamic variable"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def python_route():
    """python route for redirecting without text"""
    return redirect(url_for("python_text", text="is_cool"))


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """python route with text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)