from app import app
from flask import request

@app.route("/")
def index():
    return 'Hello!'

@app.route("/hello/<msg>", methods=["GET", 'POST'])
def hello(msg):
    return msg