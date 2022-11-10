from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.states_controller import states_bp
from controllers.areas_controller import areas_bp
# from controllers.sectors_controller import sectors_bp
# from controllers.problems_controller import problems_bp
# from controllers.ascents_controller import ascents_bp
# from controllers.climbers_controller import climbers_bp
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

    # prevents dict keys lists from auto ordering by alphabet and follows marshmallow ordering
    app.config ['JSON_SORT_KEYS'] = False
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(db_commands)
    app.register_blueprint(states_bp)
    app.register_blueprint(areas_bp)
    # app.register_blueprint(states_bp)
    # app.register_blueprint(states_bp)
    # app.register_blueprint(states_bp)
    # app.register_blueprint(states_bp)

    return app

