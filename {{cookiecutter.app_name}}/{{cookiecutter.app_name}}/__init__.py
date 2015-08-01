from flask import Flask, request
from flask_bootstrap import Bootstrap


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)

    # Load default config
    app.config.from_object('{{cookiecutter.app_name}}.config.DefaultConfig')

    # Load secret config stuff from instance folder
    app.config.from_pyfile('config.py', silent=True)

    # Permit passing in config filename for testing
    if config_filename is not None:
        app.config.from_pyfile(config_filename)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    from .views.public import public

    app.register_blueprint(public)

    @app.errorhandler(404)
    def page_not_found(error):
        return 'This route does not exist: {}'.format(request.url), 404

    return app

