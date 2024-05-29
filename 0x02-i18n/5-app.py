#!/usr/bin/env python3
"""Task 5: Mock logging in"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _
from typing import Union, Dict


class Config:
    """Configuration Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''Set user information as global variable'''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    '''Get user information based on user ID'''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Get match with the supported languages."""
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    if g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Route for the index page."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
