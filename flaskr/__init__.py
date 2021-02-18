from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    if DEBUG:
        app.config.from_object('settings.DevelopmentConfig')
    else:
        app.config.from_object('settings.ProductionConfig')
    db.init_app(app)
    CORS(app, supports_credentials=True)  # 支持跨域请求
    # 引入相关模块
    from .main.views import index
    from .login.views import login
    from .logout.views import logout
    from .register.views import register
    from .movie.views import movie
    # 注册蓝图
    app.register_blueprint(index, url_prefix='/v1/api')
    app.register_blueprint(login, url_prefix='/v1/api')
    app.register_blueprint(logout, url_prefix='/v1/api')
    app.register_blueprint(register, url_prefix='/v1/api')
    app.register_blueprint(movie, url_prefix='/v1/api')
    return app
