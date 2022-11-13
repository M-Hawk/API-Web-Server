from init import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow.validate import Length, And, Regexp

class Problem(db.Model):
    __tablename__= "problems"
    problem_id = db.Column(db.Integer, primary_key=True)
    problem_name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Integer) 
    surface_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    access = db.Column(db.Text)
    height_metres = db.Column(db.Integer)
    comments = db.Column(db.Text)
    created = db.Column(db.Date)

    sector_id = db.Column(db.Integer, db.ForeignKey("sectors.sector_id"), nullable=False)

    sector = db.relationship("Sector", back_populates="problems")
    ascents = db.relationship("Ascent", back_populates="problem", cascade="all, delete")

    @hybrid_property
    def v_grade (self):
        return f"V{self.grade}"

    @hybrid_property
    def height (self):
        return f"{self.height_metres} Metres"

class ProblemSchema(ma.Schema):

    ascents = fields.List(fields.Nested("AscentSchema", exclude=["ascent_id", "problem"]))

    v_grade = fields.String(validate=And(
        Length(min=1, max=2, error="Grade must be atleast 1 digit long, and no greater than 25 on the V Scale"),
        Regexp("^([0-9]|1[0-9]|2[0-5])$", error="Only integer numbers should be entered up to 25")
    ))
    height = fields.String(validate=And(
        Length(min=1, max=1, error="Height must be atleast 1 digit long, and no greater than 9 metres"),
        Regexp("^[0-9]+$", error="Only integer numbers should be entered up to 9 meteres")
    ))

    problem_name = fields.String(required=True, validate=And(
        Length(min=2, max=50, error="Problem Name must be at least 2 characters long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))

    class Meta:
        fields = ("problem_id", "problem_name", "v_grade", "surface_type", "description", 
        "access", "height", "comments", "sector_id", "ascents")
        ordered = True