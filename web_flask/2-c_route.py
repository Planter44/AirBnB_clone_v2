#!/usr/bin/python3
"""Starting the Flask web
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays'C' followed by <text> value."""
    return 'C ' + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
