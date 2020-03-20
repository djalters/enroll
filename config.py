import os

class Config(object)
    # security, e.g. checks against session cookie created by application
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_string"