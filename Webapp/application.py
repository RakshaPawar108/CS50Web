from flask import Flask, render_template            #someone wrote the Flask module. We import

app = Flask(__name__)           #means I want to create an app which is a flask web app __name__ represents this current file


#Flask is based on routes and route is basically part of the url that you type in in order to determine which page you want to request

#this foll part is learnt after the basic hello world stuff
@app.route("/")
def html():
    headline = "Hello, India!!"
    return render_template("hello.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye India!!!"
    return render_template("hello.html", headline=headline)
#the above html file should be stored in a new directory called templates because flask searches for that directory and runs the app
#the headline variable will exist inside html file
@app.route("/names")
def name():
    names = ["Alice", "Raksha", "Bob", "Charlie"]
    return render_template("index.html", names=names)
###############################################################
#Linking from one page to the other

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/more")
def more():
    return render_template("more.html")

###############################################################
@app.route("/hello")
def index():
    return "Hello, World!!!"

@app.route("/raksha")
def raksha():
    return "Hello, Raksha!!!"

@app.route("/david")
def david():
    return "Hello, David!!"

# Making the application more powerful now, saying hello to anyone instead of just raksha, or david etc.

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()       #capitalizes first letter of name(inbuilt)
    return  "<h1>Hello " + name + "!!!</h1>"
