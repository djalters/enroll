from application import app
from flask import render_template, request, Response, json

#moved to global space to test api
#data source, this is one record, passed as props
courseData = [
    {
        "courseID": "5887463",
        "title": "my course 10453",
        "description": "my desc",
        "credits": "100",
        "term": "1"
    },
    {
        "courseID": "234324",
        "title": "my new 3",
        "description": "my other desc",
        "credits": "400",
        "term": "5"
    }
]

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

    return render_template("courses.html", courses=True, courseData=courseData, term=term)

@app.route("/register")
def register():
    return render_template("index.html", register=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term  = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data = {"id":id, "title":title, "term":term})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx==None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")