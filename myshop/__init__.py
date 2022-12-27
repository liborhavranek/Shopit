from flask import Flask
from flask_assets import Environment, Bundle
from dotenv import load_dotenv
import scss
import os


def configure():
    load_dotenv()



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    
    # define nested Bundle


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
  'main_style': Bundle(
            'SCSS/main.scss',
            filters='libsass',
            output='Gen/main.css',
  )
} 
    assets.register(bundles)
    return app
