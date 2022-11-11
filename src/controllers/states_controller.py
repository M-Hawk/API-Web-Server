from flask import Blueprint, request
from init import db
from datetime import date
from models.states import State, StateSchema

states_bp = Blueprint("states", __name__, url_prefix="/states")

# The GET routes endpoints

# Gets all the states in the database and their areas
@states_bp.route("/", methods=["GET"])
# @jwt_required()
def get_states():
    selection = db.select(State).order_by(State.state_id)
    states = db.session.scalars(selection)
    return StateSchema(many=True).dump(states)


# Gets a state by its given ID in the database, or returns a 404 error if it does not exist
@states_bp.route("/<int:id>/", methods=["GET"])
# @jwt_required()
def get_one_state(id):
    selection = db.select(State).filter_by(state_id=id)
    state = db.session.scalar(selection)
    if state:
        return StateSchema().dump(state)
    else:
        return {"error": f"There is no state with an ID of {id}"}, 404


# The POST route endpoint
# ADD VALIDATION FOR POSTING STATES, MUST CONFORM TO NAMING CONVENTION
@states_bp.route("/", methods=["POST"])
# @jwt_required()
def create_state():
    # authorize()
    # Create a new State model instance
    info = StateSchema().load(request.json)
    # Information for the new state
    state = State(
        state_name = info["state_name"],
        state_acronym = info["state_acronym"],
        created = date.today()
        )
    # Add and commit state to DB
    db.session.add(state)
    db.session.commit()
    # Respond to admin client
    return StateSchema().dump(state), 201

@states_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_state(id):
    # authorize()
    selection = db.select(State).filter_by(state_id=id)
    state = db.session.scalar(selection)
    if state:
        state.state_name = request.json.get("state_name") or state.state_name
        state.state_acronym = request.json.get("state_acronym") or state.state_acronym
        db.session.commit()      
        return StateSchema().dump(state)
    else:
        return {'error': f'State not found with id {id}'}, 404

# The DELETE route endpoint
# Allows a single state to be deleted by its id
@states_bp.route("/<int:id>/", methods=["DELETE"])
#@jwt_required()
def delete_one_state(id):
    # sort this authorize func in auth controller later
    #authorize()
    selection = db.select(State).filter_by(state_id=id)
    state = db.session.scalar(selection)
    if state:
        db.session.delete(state)
        db.session.commit()
        return {"message": f"State {state.state_name} has been deleted successfully"}
    else:
        return {"error": f"State not found with id {id}"}, 404