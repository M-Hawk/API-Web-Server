from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.climbers import Climber, ClimberSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# WORKS COMPLETELY 
'''
Route that allows a climber to get a list of all climbers in the database, only displays climber_id and user_name
'''
@auth_bp.route("/climbers/", methods=["GET"])
@jwt_required()
def user_get_climbers():
    statement = db.select(Climber)
    climbers = db.session.scalars(statement)
    return ClimberSchema(many = True, only = ["climber_id", "user_name", "ascents"]).dump(climbers)

# WORKS COMPLETELY 
'''
Route that allows an admin to get a list of all climbers in the database
'''
@auth_bp.route("/admin/climbers/", methods=["GET"])
@jwt_required()
def admin_get_climbers():
    authorize()
    statement = db.select(Climber)
    climbers = db.session.scalars(statement)
    return ClimberSchema(many = True, exclude = ["password"]).dump(climbers)



@auth_bp.route("/register/", methods=["POST"])
def auth_register():
    try:
        info = ClimberSchema().load(request.json)
        # Create a new Climber model instance
        climber = Climber(
            email_address = info["email_address"],
            user_name = info["user_name"],
            first_name = info["first_name"],
            last_name = info["last_name"],
            password = bcrypt.generate_password_hash(info["password"]).decode("utf8")
        )
        # Add and commit climber to DB
        db.session.add(climber)
        db.session.commit()
        # Respond to client
        return ClimberSchema(exclude=["password", "ascents"]).dump(climber), 201
    except IntegrityError:
        return {"error": "Email address or User Name is already in use"}, 409


@auth_bp.route("/login/", methods=["POST"])
def auth_login():
    # Find a climber by email address
    statement = db.select(Climber).filter_by(email_address=request.json["email_address"])
    climber = db.session.scalar(statement)
    if climber and bcrypt.check_password_hash(climber.password, request.json["password"]):
        token = create_access_token(identity=str(climber.climber_id), expires_delta=timedelta(days=1))
        return {"email_address": climber.email_address, "token": token, "admin": climber.admin}
    else:
        return {"error": "Invalid email_address or password"}, 401
    

def authorize():
    id = get_jwt_identity()
    statement = db.select(Climber).filter_by(climber_id=id)
    climber = db.session.scalar(statement)
    if not climber.admin:
        abort(401)