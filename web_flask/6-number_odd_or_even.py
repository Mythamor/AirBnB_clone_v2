#!/usr/bin/python3
"""
Script that starts a Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer
            H1 tag: “Number: n” inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer
            H1 tag: “Number: n is even|odd” inside the tag BODY
Must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>")
def html_int_template(n):
    """
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html", n=n,
                           odd_or_even=odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
