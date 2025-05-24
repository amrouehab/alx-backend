#!/usr/bin/env python3
"""Flask app with parametrized templates"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine best match with supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render index.html template"""
    return render_template('3-index.html',
                           home_title=_("Welcome to ALX"),
                           home_header=_("Hello world!"))


if __name__ == '__main__':
    app.run()
