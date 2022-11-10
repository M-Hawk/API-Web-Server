from flask import Blueprint, request
from init import db
from datetime import date
from models.areas import Area, AreaSchema

areas_bp = Blueprint("areas", __name__, url_prefix="/areas")

# The GET routes endpoints

# Gets all the areas in the database and their respective sectors
@areas_bp.route("/", methods=["GET"])
def get_areas():
    selection = db.select(Area).order_by(Area.area_id)
    areas = db.session.scalars(selection)
    return AreaSchema(many=True).dump(areas)

# Gets an area by its given ID in the database, or returns a 404 error if it does not exist
@areas_bp.route("/id/<int:id>/", methods=["GET"])
def get_one_area(id):
    selection = db.select(Area).filter_by(area_id=id)
    area = db.session.scalar(selection)
    if area:
        return AreaSchema().dump(area)
    else:
        return {"error": f"There is no area with an ID of {id}"}, 404


# The POST route endpoint
# ADD VALIDATION FOR POSTING AREAS, MUST CONFORM TO NAMING CONVENTION
@areas_bp.route("/create/", methods=["POST"])
# @jwt_required()
def create_area():
    # Create a new Area model instance
    info = AreaSchema().load(request.json)

    # Information for the new area
    area = Area(
        state_id = info["state_id"],
        area_name = info["area_name"],
        description = info["description"],
        ethics = info["ethics"],
        access = info["access"],
        latitude = info["latitude"],
        longitude = info["longitude"],
        created = date.today()
        )
    # Add and commit area to DB
    db.session.add(area)
    db.session.commit()
    # Respond to admin client
    return AreaSchema().dump(area), 201


# The DELETE route endpoint
# Allows a single area to be deleted by its id
@areas_bp.route("/delete/<int:id>/", methods=["DELETE"])
#@jwt_required()
def delete_one_area(id):
    # sort this authorize func in auth controller later
    #authorize()
    selection = db.select(Area).filter_by(area_id=id)
    area = db.session.scalar(selection)
    if area:
        db.session.delete(area)
        db.session.commit()
        return {"message": f"Area {area.area_name} has been deleted successfully"}
    else:
        return {"error": f"Area not found with id {id}"}, 404