from init import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property

class Problem(db.Model):
    __tablename__= "problems"
    # Created table attributes using imported db object
    problem_id = db.Column(db.Integer, primary_key=True)
    problem_name = db.Column(db.String(50))
    grade = db.Column(db.String(4)) # Either add list of tuples or ensure V interpolated in front
    surface_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    access = db.Column(db.Text)
    height_metres = db.Column(db.Integer)
    comments = db.Column(db.Text)
    created = db.Column(db.Date)

    sector_id = db.Column(db.Integer, db.ForeignKey("sectors.sector_id"), nullable=False)

    sector = db.relationship("Sector", back_populates="problems")
    # ascents = db.relationship("Ascent", back_populates="problem", cascade="all, delete")

    @hybrid_property
    def v_grade (self):
        return f"V{self.grade}"

    @hybrid_property
    def height (self):
        return f"{self.height_metres} Metres"

class ProblemSchema(ma.Schema):

    # ascents = fields.List(fields.Nested("AscentSchema", exclude=["problem_id", "problem"]))

    class Meta:
    # Fields to expose
        fields = ("problem_id", "problem_name", "v_grade", "surface_type", "description", 
        "access", "height", "comments", "ascents")
        ordered = True