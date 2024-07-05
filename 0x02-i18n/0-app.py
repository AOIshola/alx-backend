#!/usr/bin/env python3
"""App module"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=True)
def hello():
    """Returns Basic Text"""
    return render_template("0-index.html", text="Hello World")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
