from flask import Flask, render_template, request

app = Flask(__name__)
moods = []

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/setMood")
def setMood():
    mood = request.args.get("mood")
    moods.append(mood)
    return "<p>Stimmung gespeichert!</p>" + mood


@app.route("/getMood")
def getMood():
    moodString = ", ".join(str(mood) for mood in moods)

    return "<p>Alle Stimmungen, die gespeichert wurden:<p>" + moodString