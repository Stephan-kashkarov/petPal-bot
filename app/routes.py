from app import app
from flask import request
from app.bots import lockout

state = "NO QUERY"

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
    name = request.values.get("user_name")
    text = request.values.get("text")
    return f"Hi {name}, you said {text}"

@app.route("/lockout", methods=["POST"])
def lockoutBot():
    global state
    answer, state = lockout.Bot(state, request.values.get("text")).get_func()
    print(answer, state)
    return answer