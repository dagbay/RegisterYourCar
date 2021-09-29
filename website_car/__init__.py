from flask import Flask
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager
from sqlalchemy.sql.functions import user

db = SQLAlchemy()
DB_CARS = "cars.db"

# This function will boot up the website to localhosts
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'regicar'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_CARS}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models

    create_database(app)

    # Login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

# This function creates the database for data storage
def create_database(app):
    if not path.exists('website_car/' + DB_CARS):
        db.create_all(app=app)
        print('Database created.')