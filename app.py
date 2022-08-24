from flask import Flask, render_template, request

app = Flask(__name__)
moods = []


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/setMood")
def set_mood():
    mood = int(request.args.get("mood"))
    moods.append(mood)
    return "<p>Stimmung gespeichert!</p>" + str(mood) + "<a href=\"/getMood\">get moods</a><a href=\"zurueck\"></a>"


@app.route("/getMood")
def get_mood():
    mood_string = ", ".join(str(mood) for mood in moods)

    avg = str(average_moods())

    return "<p>Alle Stimmungen, die gespeichert wurden:<p>" + mood_string + ": Durchschnitt: " + avg + "<p><a href=\"/\">Home</a></p>"


def average_moods() -> float | str:
    if len(moods) == 0:
        return 'sleeeer'

    return sum(moods) / len(moods)
