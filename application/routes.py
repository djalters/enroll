from application import app
from flask import render_template

#root directory. URL routes can be defined here. Root/index will call/render this function
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")