from init import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow.validate import Length, And, Regexp

class Area(db.Model):
    __tablename__= "areas"
    area_id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    ethics = db.Column(db.Text)
    access = db.Column(db.Text)
    latitude = db.Column(db.Float(precision=6))
    longitude = db.Column(db.Float(precision=6))
    created = db.Column(db.Date)

    state_id = db.Column(db.Integer, db.ForeignKey("states.state_id"), nullable=False)

    state = db.relationship("State", back_populates="areas")
    sectors = db.relationship("Sector", back_populates="area", cascade="all, delete")

    @hybrid_property
    def latitude_south (self):
        return f"{self.latitude} South"

    @hybrid_property
    def longitude_east (self):
        return f"{self.longitude} East"
    

class AreaSchema(ma.Schema):

    sectors = fields.List(fields.Nested("SectorSchema", exclude=["problems"]))

    area_name = fields.String(required=True, validate=And(
        Length(min=2, max=50, error="Area Name must be at least 2 characters long"),
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
        fields = ("area_id", "area_name", "description", "ethics", "access", 
        "latitude_south", "longitude_east", "state_id", "sectors")
        ordered = True
