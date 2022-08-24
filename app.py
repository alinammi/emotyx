from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/setMood")
def setMood():

    mood = request.args.get("mood")


    return "<p>Stimmung gespeichert!</p>" + mood