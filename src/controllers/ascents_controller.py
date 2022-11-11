from flask import Blueprint, request, abort
from init import db
from datetime import date
from models.ascents import Ascent, AscentSchema

ascents_bp = Blueprint("ascents", __name__, url_prefix="/ascents")


# The GET routes endpoints

# Gets all the ascents in the database
@ascents_bp.route("/", methods=["GET"])
# @jwt_required()
def get_ascents():
    selection = db.select(Ascent).order_by(Ascent.ascent_id)
    ascents = db.session.scalars(selection)
    return AscentSchema(many=True).dump(ascents)

# Gets an ascent by its given ID in the database, or returns a 404 error if it does not exist
@ascents_bp.route("/<int:id>/", methods=["GET"])
# @jwt_required()
def get_one_ascent(id):
    selection = db.select(Ascent).filter_by(ascent_id=id)
    ascent = db.session.scalar(selection)
    if ascent:
        return AscentSchema().dump(ascent)
    else:
        return {"error": f"There is no ascent with an ID of {id}"}, 404


# @ascents_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
# def update_one_ascent(id):
#         ascent_exists = db.select(Ascent).filter_by(ascent_id=id)
#         ascent = db.session.scalar(ascent_exists)
#         if ascent:
#             user_id = get_jwt_identity()
#             if ascent.climber_id != user_id:
#                 abort(401)
#             else:          
#                 ascent.tick_type = request.json.get("description") or ascent.description
#                 ascent.comments = request.json.get("comments") or ascent.comments
#                 db.session.commit()      
#                 return AscentSchema().dump(ascent)
#         else:
#             return {'error': f'Ascent not found with id {id}'}, 404


# The DELETE route endpoint
# Allows a single ascent to be deleted by its id
@ascents_bp.route("/<int:id>/", methods=["DELETE"])
# @jwt_required()
def delete_one_ascent(id):
    # authorize()
    selection = db.select(Ascent).filter_by(ascent_id=id)
    ascent = db.session.scalar(selection)
    if ascent:
        db.session.delete(ascent)
        db.session.commit()
        return {"message": f"Ascent {ascent.ascent_id} has been deleted successfully"}
    else:
        return {"error": f"Ascent not found with id {id}"}, 404
