from init import db, ma
from marshmallow import fields

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

class ProblemSchema(ma.Schema):

    sector = fields.Nested("SectorSchema", only=["sector_name"])

    class Meta:
    # Fields to expose
        fields = ("problem_id", "problem_name", "sector_id", "sector", "grade", "surface_type", "description", 
        "access", "height_metres", "comments", "created")
        ordered = True