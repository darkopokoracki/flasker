from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)


"""
--- jinja filters: -----
safe
capitalize
lower
upper
title
trim
striptags
"""

"""
{{ }} - for variables
{% %} - for logic
"""


# Create a route decorator
@app.route('/')
def index():
    first_name = 'John'
    stuff = 'this is bold text'

    favourite_pizza = ['Pepperoni', 'Cheese', 'Mexico']

    return render_template(
        'index.html',
         first_name = first_name,
         stuff = stuff,
         favourite_pizza = favourite_pizza )


# Example: localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


# Create custom error pages

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500