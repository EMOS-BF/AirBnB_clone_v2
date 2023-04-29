#!/usr/bin/python3
"""
script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes= False)
def hbnb_route():
    """
    display "Hello HBNB"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes= False)
def hbnb():
    """
    display "HBNB"
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes= False)
def c_text(text):
    """
    /c/<text>: display “C ” followed by the value 
    of the text variable (replace underscore _ symbols with a space )
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', strict_slashes= False)
@app.route('/python/<text>', strict_slashes= False)
def python_text(text="is cool"):
    """
    /python/(<text>): display “Python ”, followed 
    by the value of the text variable 
    (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes= False)
def number(n):
    """
    /number/<n>: display “n is a number” 
    only if n is an integer
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes= False)
def number_template(n):
    """
    /number_template/<n>: display 
    a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes= False)
def number_odd_even(n):
    """
    /number_odd_or_even/<n>: display a 
    HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” 
    inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
