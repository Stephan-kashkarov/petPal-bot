from app import app
from flask import request

@app.route("/")
def index():
    return 'Hello!'

@app.route("/hello", methods=["GET", 'POST'])
def hello():
    return f"Hi, {request.values.get('text')}"