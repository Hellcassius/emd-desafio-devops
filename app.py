"""
Just a simple hello-world app.
"""

from flask import Flask
import os


app = Flask(__name__)


@app.route("/")
def hello_world():
    NAME = os.getenv("NAME", "Caio")
    return f"Hello, {NAME}!"


if __name__ == "__main__":
    app.run()
