#!/usr/bin/python3
"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” (replace underscore _ symbols with a space)
use the option strict_slashes=False in your route definition
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ Return message """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Return message """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """ Return custom message """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
