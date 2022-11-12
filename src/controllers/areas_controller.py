from flask import Blueprint, request
from init import db
from datetime import date
from models.areas import Area, AreaSchema
from controllers.auth_controller import authorize
from sqlalchemy.exc import IntegrityError, DataError
from flask_jwt_extended import jwt_required

areas_bp = Blueprint("areas", __name__, url_prefix="/areas")

# The GET routes endpoints

# WORKS COMPLETELY 
'''
Route that allows a climber to get a list of all areas and their respective sectors
'''
@areas_bp.route("/", methods=["GET"])
@jwt_required()
def get_areas():
    selection = db.select(Area).order_by(Area.area_id)
    areas = db.session.scalars(selection)
    return AreaSchema(many=True).dump(areas)

# WORKS COMPLETELY 

'''
Route that allows a climber to get an area by its given ID
'''
@areas_bp.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_one_area(id):
    selection = db.select(Area).filter_by(area_id=id)
    area = db.session.scalar(selection)
    if area:
        return AreaSchema().dump(area)
    else:
        return {"error": f"There is no area with an ID of {id}"}, 404


# The POST route endpoint

# WORKS COMPLETELY 

'''
Route that allows an admin to create a new Area
'''
@areas_bp.route("/", methods=["POST"])
@jwt_required()
def create_area():
    authorize()
    try:
        info = AreaSchema().load(request.json)
        area = Area(
            state_id = info["state_id"],
            area_name = info["area_name"],
            description = request.json.get("description"),
            ethics = request.json.get("ethics"),
            access = request.json.get("access"),
            latitude = info["latitude_south"],
            longitude = info["longitude_east"],
            created = date.today()
            )
        db.session.add(area)
        db.session.commit()
        return AreaSchema().dump(area), 201
    except IntegrityError:
        return {"error": "State ID given is not in available states"}, 409
    except DataError:
        return {"error": "State ID given is not in available areas"}, 409


# The PUT/PATCH route endpoint

# WORKS COMPLETELY 

'''
Route that allows an admin to change an areas details
'''
@areas_bp.route("/<int:id>/", methods=["PUT", "PATCH"])
@jwt_required()
def update_one_area(id):
    authorize()
    selection = db.select(Area).filter_by(area_id=id)
    area = db.session.scalar(selection)
    if area:
        try:
            info = AreaSchema().load(request.json)
            area.state_id = info["state_id"] or area.state_id
            area.area_name = info["area_name"] or area.area_name
            area.description = request.json.get("description") or area.description
            area.ethics = request.json.get("ethics") or area.ethics
            area.access = request.json.get("access") or area.access
            area.latitude = info["latitude_south"] or area.latitude
            area.longitude = info["longitude_east"] or area.longitude
            db.session.commit()      
            return AreaSchema().dump(area)
        except IntegrityError:
            return {"error": "State ID given is not in available states"}, 409
        except DataError:
            return {"error": "State ID given is not in available areas"}, 409
    else:
        return {"error": f"Area not found with id {id}"}, 404


# The DELETE route endpoint

# WORKS COMPLETELY
'''
Route that allows an admin to delete an area
'''
@areas_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_one_area(id):
    authorize()
    selection = db.select(Area).filter_by(area_id=id)
    area = db.session.scalar(selection)
    if area:
        db.session.delete(area)
        db.session.commit()
        return {"message": f"Area {area.area_name} has been deleted successfully"}
    else:
        return {"error": f"Area not found with id {id}"}, 404