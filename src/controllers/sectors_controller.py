from flask import Blueprint, request
from init import db
from datetime import date
from models.sectors import Sector, SectorSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError, DataError

sectors_bp = Blueprint("sectors", __name__, url_prefix="/sectors")

# The GET routes endpoints

# WORKS COMPLETELY 
'''
Route that allows a climber to get a list of all sectors and their respective problems
'''
@sectors_bp.route("/", methods=["GET"])
@jwt_required()
def get_sectors():
    selection = db.select(Sector).order_by(Sector.sector_id)
    sectors = db.session.scalars(selection)
    return SectorSchema(many=True).dump(sectors)

# WORKS COMPLETELY 

'''
Route that allows a climber to get a sector by its given ID
'''
@sectors_bp.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_one_sector(id):
    selection = db.select(Sector).filter_by(sector_id=id)
    sector = db.session.scalar(selection)
    if sector:
        return SectorSchema().dump(sector)
    else:
        return {"error": f"There is no sector with an ID of {id}"}, 404


# The POST route endpoint

# WORKS COMPLETELY 

'''
Route that allows an admin to create a new Sector
'''
@sectors_bp.route("/", methods=["POST"])
@jwt_required()
def create_sector():
    authorize()
    try:
        info = SectorSchema().load(request.json)
        sector = Sector(
            area_id = info["area_id"],
            sector_name = info["sector_name"],
            description = request.json.get("description"),
            access = request.json.get("access"),
            latitude = info["latitude_south"],
            longitude = info["longitude_east"],
            created = date.today()
            )
        db.session.add(sector)
        db.session.commit()
        return SectorSchema().dump(sector), 201
    except IntegrityError:
        return {"error": "Area ID given is not in available areas"}, 409
    except DataError:
        return {"error": "Area ID given is not in available areas"}, 409


# The PUT/PATCH route endpoint

# WORKS COMPLETELY
'''
Route that allows an admin to change a sectors details
'''
@sectors_bp.route("/<int:id>/", methods=["PUT", "PATCH"])
@jwt_required()
def update_one_sector(id):
    authorize()
    selection = db.select(Sector).filter_by(sector_id=id)
    sector = db.session.scalar(selection)
    if sector:
        try:
            info = SectorSchema().load(request.json)
            sector.area_id = info["area_id"] or sector.area_id
            sector.sector_name =  info["sector_name"] or sector.sector_name
            sector.description = request.json.get("description") or sector.description
            sector.access = request.json.get("access") or sector.access
            sector.latitude =  info["latitude_south"] or sector.latitude
            sector.longitude =  info["longitude_east"] or sector.longitude
            db.session.commit()      
            return SectorSchema().dump(sector)
        except IntegrityError:
            return {"error": "Area ID given is not in available areas"}, 409
        except DataError:
            return {"error": "Area ID given is not in available areas"}, 409
    else:
        return {"error": f"Sector not found with id {id}"}, 404


# The DELETE route endpoint

# WORKS COMPLETELY
'''
Route that allows an admin to delete a sector
'''
@sectors_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_one_sector(id):
    authorize()
    selection = db.select(Sector).filter_by(sector_id=id)
    sector = db.session.scalar(selection)
    if sector:
        db.session.delete(sector)
        db.session.commit()
        return {"message": f"Sector {sector.sector_name} has been deleted successfully"}
    else:
        return {"error": f"Sector not found with id {id}"}, 404