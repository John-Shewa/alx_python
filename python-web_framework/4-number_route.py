#!/usr/bin/python3
""" This is a script that starts a flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ A function that returns "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ A function that returns the string "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ A function that returns a string "C" followed by
    the value of text by replacing _ with space.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>')
def python(text):
    """ A function that returns a string "Python" 
    followed by text "is cool" by replacing _ with space.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>")
def number(n=int):
    """ A function that returns an int "n" 
    followed by text "is a number ".
    """
    if n is int:
        return "{} is a number".format(n)
    else:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
