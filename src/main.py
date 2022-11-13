from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.states_controller import states_bp
from controllers.areas_controller import areas_bp
from controllers.sectors_controller import sectors_bp
from controllers.problems_controller import problems_bp
from controllers.ascents_controller import ascents_bp
from controllers.auth_controller import auth_bp
from controllers.cli_controller import db_commands
from marshmallow.exceptions import ValidationError
import os

def create_app():
    
    # Creating the flask app object
    app = Flask(__name__)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': 'You are not authorized to perform this action'}, 401

    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    # prevents dict keys lists from auto ordering by alphabet and follows marshmallow ordering
    app.config ["JSON_SORT_KEYS"] = False
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    # allows the use of JWT secret keys in the application
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    # associating database, marshmallow, bcrypt and jwt objects with our app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(db_commands)
    app.register_blueprint(states_bp)
    app.register_blueprint(areas_bp)
    app.register_blueprint(sectors_bp)
    app.register_blueprint(problems_bp)
    app.register_blueprint(ascents_bp)
    app.register_blueprint(auth_bp)

    return app

