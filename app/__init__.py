from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
photos = UploadSet('photos',IMAGES)


login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    #Initializing application
    app = Flask(__name__)

    #Creating app configuration
    app.config.from_object(config_options[config_name])


    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #Configure uploadset
    configure_uploads(app,photos)

    #Setting config

    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')
    
    return app
