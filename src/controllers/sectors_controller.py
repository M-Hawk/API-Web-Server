from flask import Blueprint, request
from init import db
from datetime import date
from models.sectors import Sector, SectorSchema

sectors_bp = Blueprint("sectors", __name__, url_prefix="/sectors")

# The GET routes endpoints

# Gets all the sectors in the database and their respective problems
@sectors_bp.route("/", methods=["GET"])
# @jwt_required()
def get_sectors():
    selection = db.select(Sector).order_by(Sector.sector_id)
    sectors = db.session.scalars(selection)
    return SectorSchema(many=True).dump(sectors)

# Gets an sector by its given ID in the database, or returns a 404 error if it does not exist
@sectors_bp.route("/id/<int:id>/", methods=["GET"])
# @jwt_required()
def get_one_sector(id):
    selection = db.select(Sector).filter_by(sector_id=id)
    sector = db.session.scalar(selection)
    if sector:
        return SectorSchema().dump(sector)
    else:
        return {"error": f"There is no sector with an ID of {id}"}, 404


# The POST route endpoint
# ADD VALIDATION FOR POSTING SECTORS, MUST CONFORM TO NAMING CONVENTION
@sectors_bp.route("/", methods=["POST"])
# @jwt_required()
def create_sector():
    #authorize()
    # Create a new Sector model instance
    info = SectorSchema().load(request.json)

    # Information for the new sector
    sector = Sector(
        area_id = info["area_id"],
        sector_name = info["sector_name"],
        description = info["description"],
        access = info["access"],
        latitude = info["latitude"],
        longitude = info["longitude"],
        created = date.today()
        )
    # Add and commit sector to DB
    db.session.add(sector)
    db.session.commit()
    # Respond to admin client
    return SectorSchema().dump(sector), 201

@sectors_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_sector(id):
    # authorize()
    selection = db.select(Sector).filter_by(sector_id=id)
    sector = db.session.scalar(selection)
    if sector:
        sector.sector_name = request.json.get("sector_name") or sector.sector_name
        sector.description = request.json.get("description") or sector.description
        sector.access = request.json.get("access") or sector.access
        sector.latitude = request.json.get("latitude") or sector.latitude
        sector.longitude = request.json.get("longitude") or sector.longitude
        db.session.commit()      
        return SectorSchema().dump(sector)
    else:
        return {'error': f'Sector not found with id {id}'}, 404


# The DELETE route endpoint
# Allows a single sector to be deleted by its id
@sectors_bp.route("/<int:id>/", methods=["DELETE"])
#@jwt_required()
def delete_one_sector(id):
    # sort this authorize func in auth controller later
    #authorize()
    selection = db.select(Sector).filter_by(sector_id=id)
    sector = db.session.scalar(selection)
    if sector:
        db.session.delete(sector)
        db.session.commit()
        return {"message": f"Sector {sector.sector_name} has been deleted successfully"}
    else:
        return {"error": f"Sector not found with id {id}"}, 404