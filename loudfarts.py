from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    return "I love to fart loud"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)