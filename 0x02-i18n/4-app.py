#!/usr/bin/env python3
'''
Flask Application

This script runs a simple Flask web
application with one route that renders an HTML template.
It includes Babel for internationalization (i18n) support.
'''

from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    Index page route.

    This function handles requests to the root URL
    ('/') and renders the '1-index.html' template.

    Returns:
        str: Rendered HTML content of '1-index.html'.
    '''
    return render_template("4-index.html")


if __name__ == '__main__':
    # Run the Flask application in debug mode.
    app.run(debug=True)
