from init import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property

class Sector(db.Model):
    __tablename__= "sectors"
    # Created table attributes using imported db object
    sector_id = db.Column(db.Integer, primary_key=True)
    sector_name = db.Column(db.String(50)) # varchar
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

    class Meta:
    # Fields to expose
        fields = ("sector_id", "sector_name", "description", "access", 
        "latitude_south", "longitude_east", "problems")
        ordered = True

