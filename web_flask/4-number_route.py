#!/usr/bin/python3
"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” (replace underscore _ symbols with a space)
        /python/<text>: display “Python ”, replace underscore with a space
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
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


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """ Return a custom message """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    """ Display text n is a number if int"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

