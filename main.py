from flask import Flask

# identify class being passed to flask
app = Flask(__name__)

#root directory. URL routes can be defined here. Root/index will call/render this function
@app.route("/")
@app.route("/index")
def index():
    return "<h1>hello</h1>"