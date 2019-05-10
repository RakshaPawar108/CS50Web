import datetime                     #to get current date easily

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()           #getting current date and time and store it in time
    new_year = now.month == 1 and now.day == 1          #bool variable new_year will check if date and month are true and will store value
   # new_year = True
    return render_template("newyear.html", new_year=new_year)
