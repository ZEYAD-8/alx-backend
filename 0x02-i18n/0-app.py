#!/usr/bin/env python3
"""
Flask Application

This script runs a simple Flask web
application with one route that renders an HTML template.
"""


from flask import Flask, render_template


# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    """
    Index page route.

    This function handles requests to the
    root URL ('/') and renders the '0-index.html' template.

    Returns:
        str: Rendered HTML content of '0-index.html'.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    # Run the Flask application in debug mode.
    app.run(debug=True)
