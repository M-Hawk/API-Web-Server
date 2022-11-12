from flask import Blueprint, request
from main import db
from datetime import date
from models.problems import Problem, ProblemSchema
from models.ascents import Ascent, AscentSchema
from controllers.auth_controller import authorize
from sqlalchemy.exc import IntegrityError, DataError

from flask_jwt_extended import jwt_required, get_jwt_identity

problems_bp = Blueprint("problems", __name__, url_prefix="/problems")

# The GET routes endpoints

# WORKS COMPLETELY 
'''
Route that allows a climber to get a list of all problems and their respective ascents
'''
@problems_bp.route("/", methods=["GET"])
@jwt_required()
def get_problems():
    selection = db.select(Problem).order_by(Problem.problem_id)
    problems = db.session.scalars(selection)
    return ProblemSchema(many=True).dump(problems)

# WORKS COMPLETELY 
'''
Route that allows a climber to get a sector by its given ID
'''
@problems_bp.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_one_problem(id):
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    if problem:
        return ProblemSchema().dump(problem)
    else:
        return {"error": f"There is no problem with an ID of {id}"}, 404


# The POST route endpoint

# WORKS COMPLETELY

'''
Route that allows an admin to create a new Problem
'''
@problems_bp.route("/", methods=["POST"])
@jwt_required()
def create_problem():
    authorize()
    try:
        info = ProblemSchema().load(request.json)
        problem = Problem(
            sector_id = info["sector_id"],
            problem_name = info["problem_name"],
            description = request.json.get("description"),
            surface_type = request.json.get("surface_type"),
            access = request.json.get("access"),
            grade = info["v_grade"],
            height_metres = info["height"],
            comments = request.json.get("comments"),
            created = date.today()
            )
        db.session.add(problem)
        db.session.commit()
        return ProblemSchema().dump(problem), 201
    except IntegrityError:
        return {"error": "Sector ID given is not in available areas"}, 409
    except DataError:
        return {"error": "Sector ID given is not in available areas"}, 409



# The PUT/PATCH route endpoint

# UP TO HERE

@problems_bp.route("/<int:id>/", methods=["PUT", "PATCH"])
@jwt_required()
def update_one_problem(id):
    authorize()
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    if problem:
        problem.problem_name = request.json.get("problem_name") or problem.problem_name
        problem.description = request.json.get("description") or problem.description
        problem.access = request.json.get("access") or problem.access
        db.session.commit()      
        return ProblemSchema().dump(problem)
    else:
        return {"error": f"Problem not found with id {id}"}, 404

# The DELETE route endpoint
# Allows a single problem to be deleted by its id
@problems_bp.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_one_problem(id):
    authorize()
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
@jwt_required()
def get_problem_ascents(id):
    selection = db.select(Problem).filter_by(problem_id = id)
    problem = db.session.scalar(selection)
    return AscentSchema(many = True, exclude = ["problem"]).dump(problem.ascents)


# WORKS COMPLETELY 
'''
Route that allows a climber to add an ascent linked to their id by its problem id
'''
@problems_bp.route("/<int:id>/ascents/", methods=["POST"])
@jwt_required()
def create_ascent(id):
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    # Information for the new ascent
    if problem:
        info = AscentSchema().load(request.json)
        ascent = Ascent(
            climber_id = get_jwt_identity(),
            problem_id = problem.problem_id,
            tick_type = info["tick_type"],
            comments = info["comments"],
            created = date.today()
        )
        # Add and commit ascent to DB
        db.session.add(ascent)
        db.session.commit()
        # Respond to client
        return AscentSchema().dump(ascent), 201
    else:
        return {"error": f"Problem not found with id {id}"}, 404
