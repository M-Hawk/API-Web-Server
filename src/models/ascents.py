from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import OneOf
from marshmallow.exceptions import ValidationError

VALID_TICK_TYPES = ("Send", "Dab", "Repeat", "Onsight", "Flash", "Redpoint", "First Ascent", "Attempt", "Working", "Retreat")

class Ascent(db.Model):
    __tablename__= "ascents"
    ascent_id = db.Column(db.Integer, primary_key=True)
    tick_type = db.Column(db.String, nullable=False, default=VALID_TICK_TYPES[0])
    comments = db.Column(db.Text)
    created = db.Column(db.Date)

    climber_id = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey("problems.problem_id"), nullable=False)

    problem = db.relationship("Problem", back_populates="ascents")
    climber = db.relationship("Climber", back_populates="ascents")

class AscentSchema(ma.Schema):

    problem = fields.Nested("ProblemSchema", only=["problem_id", "problem_name", "v_grade"])
    climber = fields.Nested("ClimberSchema", only=["climber_id", "user_name"])

    tick_type = fields.String(load_default=VALID_TICK_TYPES[0], validate=OneOf(VALID_TICK_TYPES))

    class Meta:
        fields = ("ascent_id", "climber", "problem", "tick_type", "comments", "created")
        ordered = True


