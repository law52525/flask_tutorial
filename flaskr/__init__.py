import os
from flask import Flask


def create_app(test_config=None):
    # instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。实例文件夹在 flaskr 包的外面
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return "Hello World!"

    return app

