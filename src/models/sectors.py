from init import db, ma
from marshmallow import fields

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

class SectorSchema(ma.Schema):

    area = fields.Nested("AreaSchema", only=["area_name"])

    class Meta:
    # Fields to expose
        fields = ("sector_id", "sector_name", "area_id", "area", "description", "access", 
        "latitude", "longitude", "created")
        ordered = True