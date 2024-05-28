#!/usr/bin/env python3
"""
Basic Babel setup.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration  for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(
            app.config['LANGUAGES']
            )


@app.route('/')
def index():
    """Route for the index page."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
