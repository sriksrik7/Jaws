from flask import Flask
from SharkAttackRepo import SharkAttackRepo

app = Flask(__name__)
repo = SharkAttackRepo()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
