from app import app
from flask import request

@app.route("/")
def index():
    return 'Hello!'

@app.route("/hello", methods=["GET", 'POST'])
def hello():
    return f"Hi, {request.values.get('text')}"

@app.route("/weather", methods=["GET", 'POST'])
def weather():
    temp = int(request.values.get('temp'))
    return f"The temp is {temp}" if temp < 30 else "Its Hot!"

@app.route("/talk", methods=["POST"])
def talk():
    name = request.values
    return "name"