from flask import Blueprint, request
from main import db
from datetime import date
from models.problems import Problem, ProblemSchema
from models.ascents import Ascent, AscentSchema

problems_bp = Blueprint("problems", __name__, url_prefix="/problems")

# The GET routes endpoints

# Gets all the problems in the database and their respective ascents
@problems_bp.route("/", methods=["GET"])
# @jwt_required()
def get_problems():
    selection = db.select(Problem).order_by(Problem.problem_id)
    problems = db.session.scalars(selection)
    return ProblemSchema(many=True).dump(problems)

# Gets an problem by its given ID in the database, or returns a 404 error if it does not exist
@problems_bp.route("/<int:id>/", methods=["GET"])
# @jwt_required()
def get_one_problem(id):
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    if problem:
        return ProblemSchema().dump(problem)
    else:
        return {"error": f"There is no problem with an ID of {id}"}, 404


# The POST route endpoint
# ADD VALIDATION FOR POSTING PROBLEMS, MUST CONFORM TO NAMING CONVENTION
@problems_bp.route("/", methods=["POST"])
# @jwt_required()
def create_problem():
    #authorize()
    # Create a new problem model instance
    info = ProblemSchema().load(request.json)

    # Information for the new problem
    problem = Problem(
        sector_id = info["sector_id"],
        problem_name = info["problem_name"],
        description = info["description"],
        access = info["access"],
        latitude = info["latitude"],
        longitude = info["longitude"],
        created = date.today()
        )
    # Add and commit problem to DB
    db.session.add(problem)
    db.session.commit()
    # Respond to admin client
    return ProblemSchema().dump(problem), 201


@problems_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_problem(id):
    # authorize()
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    if problem:
        problem.problem_name = request.json.get("problem_name") or problem.problem_name
        problem.description = request.json.get("description") or problem.description
        problem.access = request.json.get("access") or problem.access
        problem.latitude = request.json.get("latitude") or problem.latitude
        problem.longitude = request.json.get("longitude") or problem.longitude
        db.session.commit()      
        return ProblemSchema().dump(problem)
    else:
        return {'error': f'Problem not found with id {id}'}, 404

# The DELETE route endpoint
# Allows a single problem to be deleted by its id
@problems_bp.route("/<int:id>/", methods=["DELETE"])
#@jwt_required()
def delete_one_problem(id):
    # sort this authorize func in auth controller later
    #authorize()
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    if problem:
        db.session.delete(problem)
        db.session.commit()
        return {"message": f"Problem {problem.problem_name} has been deleted successfully"}
    else:
        return {"error": f"Problem not found with id {id}"}, 404



# Ascent routes related to problems


# Gets ascents by their related problems
@problems_bp.route("/<int:id>/ascents/", methods=["GET"])
# @jwt_required()
def get_problem_ascents(id):
    selection = db.select(Problem).filter_by(problem_id = id)
    problem = db.session.scalar(selection)
    return AscentSchema(many = True, exclude = ["problem"]).dump(problem.ascents)


# ADD VALIDATION FOR POSTING ASCENTS, MUST CONFORM TO NAMING CONVENTION
@problems_bp.route("/<int:id>/ascents/", methods=["POST"])
# @jwt_required()
def create_ascent(id):
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    # Information for the new ascent
    if problem:
        ascent = Ascent(
            climber_id = request.json["climber_id"], #  sort climber id to get_jwt_identity()
            problem_id = problem.problem_id,
            tick_type = request.json["tick_type"],
            comments = request.json["comments"],
            created = date.today()
        )
        # Add and commit ascent to DB
        db.session.add(ascent)
        db.session.commit()
        # Respond to client
        return AscentSchema().dump(ascent), 201
    else:
        return {'error': f'Problem not found with id {id}'}, 404
