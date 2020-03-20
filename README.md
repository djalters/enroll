# enroll
Full-stack web dev with flask

*prerequsite*
* OS Ubuntu 1804
* python3 -> pip -> venv

*install venv*
* flask (microframework)
* flask-wtf (for forms)
* python-dotenv (so .flaskenv file can be read)


Create .flaskenv, add parameters
`pip freeze` create requirements file

003_createRunSimpleFlask
`flask run` (in venv)
* lazyloading
* debug mode (default) rerenders changes to files on dev server
* path routing via decorators

004_createEnrollApp
* application package/folder created
   * main.py draws on application code - common pattern, e.g. node
   * init.py, index required for each package, init allows initalisation
   * templates folder (html jinja templates)
   * static (static web files)
* main.py
   * moved main code into init.py for application
   * set import in main, import app