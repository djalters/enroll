from application import app
from flask import render_template

#root directory. URL routes can be defined here. Root/index will call/render this function
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index = True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/courses")
def courses():
    return render_template("courses.html", courses=True)

@app.route("/register")
def register():
    return render_template("index.html", register=True)