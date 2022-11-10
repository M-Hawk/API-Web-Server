from flask import Blueprint, request
from main import db
from datetime import date
from models.problems import Problem, ProblemSchema

problems_bp = Blueprint("problems", __name__, url_prefix="/problems")

# The GET routes endpoints

# Gets all the problems in the database and their respective ascents
@problems_bp.route("/", methods=["GET"])
def get_problems():
    selection = db.select(Problem).order_by(Problem.problem_id)
    problems = db.session.scalars(selection)
    return ProblemSchema(many=True).dump(problems)

# Gets an problem by its given ID in the database, or returns a 404 error if it does not exist
@problems_bp.route("/id/<int:id>/", methods=["GET"])
def get_one_problem(id):
    selection = db.select(Problem).filter_by(problem_id=id)
    problem = db.session.scalar(selection)
    if problem:
        return ProblemSchema().dump(problem)
    else:
        return {"error": f"There is no problem with an ID of {id}"}, 404


# The POST route endpoint
# ADD VALIDATION FOR POSTING PROBLEMS, MUST CONFORM TO NAMING CONVENTION
@problems_bp.route("/create/", methods=["POST"])
# @jwt_required()
def create_problem():
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


# The DELETE route endpoint
# Allows a single problem to be deleted by its id
@problems_bp.route("/delete/<int:id>/", methods=["DELETE"])
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