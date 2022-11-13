from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.climbers import Climber, ClimberSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# The GET route endpoints

'''
Route that allows a climber to get a list of all climbers in the database, only displays climber_id and user_name
'''
@auth_bp.route("/climbers/", methods=["GET"])
@jwt_required()
def user_get_climbers():
    statement = db.select(Climber)
    climbers = db.session.scalars(statement)
    return ClimberSchema(many = True, only = ["climber_id", "user_name", "ascents"]).dump(climbers)


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


# The POST route endpoints

'''
Route that allows any potential user of the API to register a climber account in the database
'''
@auth_bp.route("/register/", methods=["POST"])
def auth_register():
    try:
        info = ClimberSchema().load(request.json)
        climber = Climber(
            email_address = info["email_address"],
            user_name = info["user_name"],
            first_name = info["first_name"],
            last_name = info["last_name"],
            password = bcrypt.generate_password_hash(info["password"]).decode("utf8"),
        )
        db.session.add(climber)
        db.session.commit()
        return ClimberSchema(exclude=["password", "ascents", "admin"]).dump(climber), 201
    except IntegrityError:
        return {"error": "Email address or User Name is already in use"}, 409



'''
Route that allows an admin to register another admin account in the database
'''
@auth_bp.route("/register/admin", methods=["POST"])
@jwt_required()
def auth_register_admin():
    authorize()
    try:
        info = ClimberSchema().load(request.json)
        admin = Climber(
            email_address = info["email_address"],
            user_name = info["user_name"],
            first_name = info["first_name"],
            last_name = info["last_name"],
            admin = True,
            password = bcrypt.generate_password_hash(info["password"]).decode("utf8"),
        )
        db.session.add(admin)
        db.session.commit()
        return ClimberSchema(exclude=["password", "ascents"]).dump(admin), 201
    except IntegrityError:
        return {"error": "Email address or User Name is already in use"}, 409



'''
Route that allows a climber account in the database
'''
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


# The PUT/PATCH route endpoint

'''
Route that allows a climber to change their climber details
'''
@auth_bp.route("/<int:id>/", methods=["PUT", "PATCH"])
@jwt_required()
def update_own_details(id):
        climber_exists = db.select(Climber).filter_by(climber_id=id)
        climber = db.session.scalar(climber_exists)
        if climber:
            user_id = int(get_jwt_identity())
            if climber.climber_id != user_id:
                abort(401)
            else:
                info = ClimberSchema().load(request.json)
                climber.email_address = info["email_address"] or climber.email_address
                climber.user_name = info["user_name"] or climber.user_name
                climber.password = bcrypt.generate_password_hash(info["password"]).decode("utf8") or climber.password
                climber.first_name = info["first_name"] or climber.first_name
                climber.last_name = info["last_name"] or climber.last_name
                db.session.commit()      
                return ClimberSchema(exclude=["password", "ascents"]).dump(climber)
        else:
            return {"error": f"Ascent not found with id {id}"}, 404


# The DELETE route endpoints

'''
Route that allows an admin to delete a climber user
'''
@auth_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_one_climber(id):
    authorize()
    selection = db.select(Climber).filter_by(climber_id=id)
    climber = db.session.scalar(selection)
    if climber:
        db.session.delete(climber)
        db.session.commit()
        return {"message": f"Climber, {climber.user_name} has been deleted successfully"}
    else:
        return {"error": f"Climber not found with id {id}"}, 404


'''
Route that allows a climber who owns that particular ascent to delete it
'''
@auth_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_own_account(id):
        account_exists = db.select(Climber).filter_by(climber_id=id)
        climber = db.session.scalar(account_exists)
        if climber:
            user_id = int(get_jwt_identity())
            if climber.climber_id != user_id:
                abort(401)
            else:          
                db.session.delete(climber)
                db.session.commit()
                return {"message": f"Climber, {climber.user_name} has been deleted successfully"}
        else:
            return {"error": f"Climber not found with id {id}"}, 404

# Function for authorization

'''
Function that authorizes administrators to access admin routes
'''
def authorize():
    id = get_jwt_identity()
    statement = db.select(Climber).filter_by(climber_id=id)
    climber = db.session.scalar(statement)
    if not climber.admin:
        abort(401)