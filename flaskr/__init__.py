import os
from flask import Flask
from .main.views import index
from .login.views import login
from .logout.views import logout
from .register.views import register

def create_app():
    app = Flask(__name__)
    DEBUG = True
    if DEBUG:
        app.config.from_object('settings.DevelopmentConfig')
    else:
        app.config.from_object('settings.ProductionConfig')

    app.register_blueprint(index, url_prefix='/api')
    app.register_blueprint(login, url_prefix='/api')
    app.register_blueprint(logout, url_prefix='/api')
    app.register_blueprint(register, url_prefix='/api')
    return app