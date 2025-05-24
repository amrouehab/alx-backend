#!/usr/bin/env python3
"""Flask app with user locale preference"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """Config class for Flask app"""
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


def get_user() -> dict:
    """Get user dictionary or None if ID not found"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """Set user as global on flask.g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine best match with supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render index.html template"""
    return render_template('6-index.html',
                           home_title=_("Welcome to ALX"),
                           home_header=_("Hello world!"),
                           logged_in_as=_("You are logged in as %(username)s."),
                           not_logged_in=_("You are not logged in."))


if __name__ == '__main__':
    app.run()
