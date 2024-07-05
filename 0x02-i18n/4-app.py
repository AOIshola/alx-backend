#!/usr/bin/env python3
"""4-app Module"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
config = Config()
app.config.from_object(Config)
babel = Babel(app, default_locale='en', default_timezone='UTC')


@babel.localeselector
def get_locale():
    """get supported languages"""
    locale = request.args.get('locale')

    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=True)
def hello():
    """Returns Basic Text"""
    return render_template("4-index.html", text=_("Hello World!"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
