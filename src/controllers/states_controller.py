from flask import Blueprint, request
from init import db
from datetime import date
from models.states import State, StateSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

states_bp = Blueprint("states", __name__, url_prefix="/states")

# The GET routes endpoints
 
'''
Route that allows a climber to get a list of all states and their respective areas
'''
@states_bp.route("/", methods=["GET"])
@jwt_required()
def get_states():
    selection = db.select(State).order_by(State.state_id)
    states = db.session.scalars(selection)
    return StateSchema(many=True).dump(states)

 
'''
Route that allows a climber to get a state by its given ID
'''
@states_bp.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_one_state(id):
    selection = db.select(State).filter_by(state_id=id)
    state = db.session.scalar(selection)
    if state:
        return StateSchema().dump(state)
    else:
        return {"error": f"There is no state with an ID of {id}"}, 404


# The POST route endpoint

'''
Route that allows an admin to post a state
'''
@states_bp.route("/", methods=["POST"])
@jwt_required()
def create_state():
    authorize()
    info = StateSchema().load(request.json)
    state = State(
        state_name = info["state_name"],
        state_acronym = info["state_acronym"],
        created = date.today()
        )
    db.session.add(state)
    db.session.commit()
    return StateSchema().dump(state), 201

# The PUT/PATCH route endpoint

'''
Route that allows an admin to change a states details
'''
@states_bp.route("/<int:id>/", methods=["PUT", "PATCH"])
@jwt_required()
def update_one_state(id):
    authorize()
    selection = db.select(State).filter_by(state_id=id)
    state = db.session.scalar(selection)
    if state:
        info = StateSchema().load(request.json)
        state.state_name = info["state_name"] or state.state_name
        state.state_acronym = info["state_acronym"] or state.state_acronym
        db.session.commit()      
        return StateSchema().dump(state)
    else:
        return {"error": f"State not found with id {id}"}, 404


# The DELETE route endpoint

'''
Route that allows an admin to delete a state
'''
@states_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_one_state(id):
    authorize()
    selection = db.select(State).filter_by(state_id=id)
    state = db.session.scalar(selection)
    if state:
        db.session.delete(state)
        db.session.commit()
        return {"message": f"State, {state.state_name} has been deleted successfully"}
    else:
        return {"error": f"State not found with id {id}"}, 404