#!/usr/bin/env python3
"""4-app Module"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
config = Config()
app.config.from_object(Config)
babel = Babel(app, default_locale='en', default_timezone='UTC')

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
        # if user_id is None or user_id not in users:
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """Gets executed before request is processed"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user')
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=True)
def hello():
    """Returns Basic Text"""
    return render_template("5-index.html", text=_("Hello World!"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
