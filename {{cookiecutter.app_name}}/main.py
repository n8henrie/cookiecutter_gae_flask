from google.appengine.ext.webapp.util import run_wsgi_app
from {{cookiecutter.app_name}} import create_app

app = create_app()
run_wsgi_app(app)
