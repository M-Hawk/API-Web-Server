from init import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow.validate import Length, And, Regexp

class Sector(db.Model):
    __tablename__= "sectors"
    # Created table attributes using imported db object
    sector_id = db.Column(db.Integer, primary_key=True)
    sector_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    access = db.Column(db.Text)
    latitude = db.Column(db.Float(precision=6))
    longitude = db.Column(db.Float(precision=6))
    created = db.Column(db.Date)

    area_id = db.Column(db.Integer, db.ForeignKey("areas.area_id"), nullable=False)

    area = db.relationship("Area", back_populates="sectors")
    problems = db.relationship("Problem", back_populates="sector", cascade="all, delete")


    @hybrid_property
    def latitude_south (self):
        return f"{self.latitude} South"

    @hybrid_property
    def longitude_east (self):
        return f"{self.longitude} East"

class SectorSchema(ma.Schema):

    problems = fields.List(fields.Nested("ProblemSchema", exclude=["ascents"]))

    sector_name = fields.String(required=True, validate=And(
        Length(min=2, max=50, error="Sector Name must be at least 2 characters long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))

    latitude_south = fields.String(validate=And(
        Length(min=6, max=16, error="Latitude must be at least 6 digits long, and no greater than 16"),
        Regexp("[+-]?[0-9]+\.[0-9]+", error="Only decimal point numbers should be entered")
    ))       

    longitude_east = fields.String(validate=And(
        Length(min=6, max=16, error="Longitude must be at least 6 digits long, and no greater than 16"),
        Regexp("[+-]?[0-9]+\.[0-9]+", error="Only decimal point numbers should be entered")
    ))

    class Meta:
        fields = ("sector_id", "sector_name", "description", "access", 
        "latitude_south", "longitude_east", "area_id", "problems")
        ordered = True

