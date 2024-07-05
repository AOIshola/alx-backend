#!/usr/bin/env python3
"""1-app Module"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_pyfile('config.py')
babel = Babel(app, default_locale='en', default_timezone='UTC')


@app.route('/', strict_slashes=True)
def hello():
    """Returns Basic Text"""
    return render_template("1-index.html", text="Hello World")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
