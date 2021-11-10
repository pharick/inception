from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.wsgi_app = ReverseProxied(app.wsgi_app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE_USER='short_urls',
        DATABASE_PASSWORD='',
        DATABASE_DB='short_urls',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'mysql+pymysql://{app.config["DATABASE_USER"]}:' \
        f'{app.config["DATABASE_PASSWORD"]}@{app.config["DATABASE_SERVER"]}/' \
        f'{app.config["DATABASE_DB"]}?charset=utf8mb4'

    from . import views
    app.register_blueprint(views.bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
