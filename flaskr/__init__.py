import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    print(os.path.join(app.instance_path, 'flaskr.sqlite'))
    app.config.update(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "hello, world"
    from . import db
    db.init_app(app)

    return app
