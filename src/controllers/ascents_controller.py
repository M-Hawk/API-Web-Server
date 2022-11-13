from flask import Blueprint, request, abort
from init import db
from datetime import date
from models.ascents import Ascent, AscentSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required, get_jwt_identity

ascents_bp = Blueprint("ascents", __name__, url_prefix="/ascents")

# The GET route endpoints

'''
Route that allows a climber to get a list of all ascents
'''
@ascents_bp.route("/", methods=["GET"])
@jwt_required()
def get_ascents():
    selection = db.select(Ascent).order_by(Ascent.ascent_id)
    ascents = db.session.scalars(selection)
    return AscentSchema(many=True).dump(ascents)
 
'''
Route that allows a climber to get an ascent by its given ID
'''
@ascents_bp.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_one_ascent(id):
    selection = db.select(Ascent).filter_by(ascent_id=id)
    ascent = db.session.scalar(selection)
    if ascent:
        return AscentSchema().dump(ascent)
    else:
        return {"error": f"There is no ascent with an ID of {id}"}, 404

# The PUT/PATCH route endpoint

'''
Route that allows a climber who owns that particular ascent to change its details
'''
@ascents_bp.route("/<int:id>/", methods=["PUT", "PATCH"])
@jwt_required()
def update_own_ascent(id):
        ascent_exists = db.select(Ascent).filter_by(ascent_id=id)
        ascent = db.session.scalar(ascent_exists)
        if ascent:
            user_id = int(get_jwt_identity())
            if ascent.climber_id != user_id:
                abort(401)
            else:
                info = AscentSchema().load(request.json)
                ascent.tick_type = info["tick_type"] or ascent.tick_type
                ascent.comments = info["comments"] or ascent.comments
                db.session.commit()      
                return AscentSchema().dump(ascent)
        else:
            return {"error": f"Ascent not found with id {id}"}, 404

# The DELETE route endpoints

'''
Route that allows a climber who owns that particular ascent to delete it
'''
@ascents_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_own_ascent(id):
        ascent_exists = db.select(Ascent).filter_by(ascent_id=id)
        ascent = db.session.scalar(ascent_exists)
        if ascent:
            user_id = int(get_jwt_identity())
            if ascent.climber_id != user_id:
                abort(401)
            else:          
                db.session.delete(ascent)
                db.session.commit()
                return {"message": f"Ascent, {ascent.ascent_id} has been deleted successfully"}
        else:
            return {"error": f"Ascent not found with id {id}"}, 404


'''
Route that allows an admin to delete a single ascent by its id
'''
@ascents_bp.route("/admin/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_one_ascent(id):
    authorize()
    selection = db.select(Ascent).filter_by(ascent_id=id)
    ascent = db.session.scalar(selection)
    if ascent:
        db.session.delete(ascent)
        db.session.commit()
        return {"message": f"Ascent, {ascent.ascent_id} has been deleted successfully"}
    else:
        return {"error": f"Ascent not found with id {id}"}, 404



