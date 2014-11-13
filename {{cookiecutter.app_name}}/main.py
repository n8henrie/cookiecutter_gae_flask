from google.appengine.ext.webapp.util import run_wsgi_app
from {{cookiecutter.app_name}}.settings import DevConfig
from {{cookiecutter.app_name}}.app import create_app

# app = create_app(config_object=DevConfig())
app = create_app()
run_wsgi_app(app)
