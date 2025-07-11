#!/usr/bin/env python3
"""Basic Flask app for ALX welcome page."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """Render the welcome page."""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()

