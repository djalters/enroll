from application import app
from flask import render_template, request

#root directory. URL routes can be defined here. Root/index will call/render this function
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index = True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Fall 2019"):
    #data source, this is one record, passed as props
    courseData = [
        {
            "courseID": "5887463",
            "title": "my course 10453",
            "description": "my desc",
            "credits": "100",
            "term": "1"
        }
    ]

    return render_template("courses.html", courses=True, courseData=courseData, term=term)

@app.route("/register")
def register():
    return render_template("index.html", register=True)

@app.route("/enrollment")
def enrollment():
    id = request.args.get('courseID')
    title = request.args.get('title')
    term  = request.args.get('term')
    return render_template("enrollment.html", enrollment=True, data = {"id":id, "title":title, "term":term})