from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def notess():
    if session.get("notes") is None:
        session["notes"] = []           #notes particular to my session only. no one else can see it from their session
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)       #append notes particular to my session only

    return render_template("notes.html", notes=session["notes"])
