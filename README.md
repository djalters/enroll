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
   * static (static web files) with css and images folders
* main.py
   * moved main code into init.py for application
   * set import in main, import app
* config.py module
   * top level class to hold KeyVals, e.g. security strings, db connections
* routes.py module for all routing patterns
* modify __init__.py, now only holds flask app variable, and references routes - builds up bigger file with seperation of concerns
* Navigation Links
   * `url_for` resolve links - index function for endpoints, return a rendered page in this instance
   * route() binds functions to 1+ URL patterns
   * jinja delimiters

005_workingWithTemplates
* Jinja inheritance logic
* create base template
   * e.g. a file called 'base' or 'layout' which holds common page structure, naviagation etc
   * these are imported and file content rendered within block statement
* template inheritance creates child templates
   * child templates for login, classes and register pages
* pass data to view (templates) using props
   * passing data from source to view, e.g. 
      * route function pass data to a page template in props
   * higlighting active menu item
      * route function pass flag to page
      * nested if statement within html element controls behaviour
   * for directive
   * course table with json dta
* access data via request/response objects
   * access query string (GET) url parameters
      * request.args.get(<fieldname>)
   * flask reponse object class flask.response