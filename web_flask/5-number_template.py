#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
    displays “Hello HBNB!”
    in the route page
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb1():
    """
    display "HBNB"
    in the route page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    display “C ” followed by the value of the text variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    The default value of text is “is cool”
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def isitanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
