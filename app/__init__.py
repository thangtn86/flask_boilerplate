# coding: utf-8
import os
import sys
from config import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(APP_DIR)

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = ''
mail = Mail()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # initialize app
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    # import blueprints
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
