from flask import Flask, render_template, request
#request represents requests made by the user so its imported

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/xyz", methods=["GET", "POST"])
def xyz():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("xyz.html", name=name)
