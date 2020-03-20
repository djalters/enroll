from flask import Flask

# identify class being passed to flask
app = Flask(__name__)

# all routes happen in routes.py
from application import routes