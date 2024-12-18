#!/usr/bin/env python3
'''
Flask Application

This script runs a simple Flask web
application with one route that renders an HTML template.
It includes Babel for internationalization (i18n) support.
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    '''
    Configuration class for Flask application

    This class contains configuration
    settings for available languages,
    default locale, and default timezone.
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False  # Disable strict slashes

# Instantiate Babel and store it in a module-level variable named babel
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''
    Get user function.

    This function returns a user dictionary
    based on the user ID from the request.

    Returns:
        dict: User dictionary.
    '''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    '''
    Before request function.

    This function sets the current user
    based on the user ID from the request.
    '''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    '''
    Get locale function.

    This function returns the current locale.

    It uses the 'Accept-Language' header
    from the request to determine the best match
    from the available languages configured in the app.

    Returns:
        str: Current locale.
    '''
    loacle = request.args.get('locale')
    if loacle in app.config['LANGUAGES']:
        return loacle
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    request_locales = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if request_locales:
        return request_locales
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''
    Index page route.

    This function handles requests to the root URL
    ('/') and renders the '1-index.html' template.

    Returns:
        str: Rendered HTML content of '1-index.html'.
    '''
    return render_template("5-index.html")


if __name__ == '__main__':
    # Run the Flask application in debug mode.
    app.run(debug=True)
