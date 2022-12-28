from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from os import path
import scss
import os


def configure():
    load_dotenv()
    
    
db = SQLAlchemy()
DB_NAME = "myshop.db"

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    from .models import Costumer
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return Costumer.query.get(id)


    from .admin import admin
    from .products import products
    from .views import views
    from .auth import auth

    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(products, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    
    assets = Environment(app) # create an Environment instance

    bundles = {  # define nested Bundle
  'your_style': Bundle(
            'SCSS/your.scss',
            filters='libsass',
            output='Gen/your.css',
  ),
  'register_style': Bundle(
            'SCSS/register.scss',
            filters='libsass',
            output='Gen/register.css',
  )
} 
    assets.register(bundles)
    return app


def create_database(app):
    if not path.exists('shop/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')