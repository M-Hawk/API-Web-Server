from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.states_controller import states_bp
from controllers.cli_controller import db_commands
from marshmallow.exceptions import ValidationError
import os

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # associating database, marshmallow, bcrypt and jwt objects with our app


    # import the controllers and activate the blueprints

    # app.register_blueprint(cards_bp)
    # app.register_blueprint(auth_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(db_commands)
    app.register_blueprint(states_bp)

    return app

