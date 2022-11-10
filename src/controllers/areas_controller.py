from flask import Blueprint, request
from init import db

from models.areas import Area, AreaSchema


areas_bp = Blueprint('areas', __name__, url_prefix='/areas')

# The GET routes endpoints

# Gets all the states in the database and their areas
@areas_bp.route('/', methods=['GET'])
def get_areas():
    selection = db.select(Area).order_by(Area.area_id)
    areas = db.session.scalars(selection)
    return AreaSchema(many=True).dump(areas)

