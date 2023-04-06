import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf.csrf import CSRFProtect

#  define all the tools that has been used

db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()

# create init app for dev, test or prod
def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    app.config.from_pyfile(configuration)

    db.init_app(app) # bind database to flask app
    bootstrap.init_app(app) # initalize bootstarp
    

# import app and register blueprint

    from app.citybike import main
    app.register_blueprint(main)


    return app