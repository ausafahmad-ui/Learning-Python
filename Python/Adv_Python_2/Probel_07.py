from flask import Flask

First = Flask(__name__)

@First.route("/")
def hello_world():
    return "<p>Hello, Ausaf.This is your first server program and you are seeing it on your local host!</p>"
First.run()