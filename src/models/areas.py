from init import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property

class Area(db.Model):
    __tablename__= "areas"
    # Created table attributes using imported db object
    area_id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(50)) # varchar
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

    class Meta:
    # Fields to expose
        fields = ("area_id", "area_name", "description", "ethics", "access", 
        "latitude_south", "longitude_east", "sectors")
        ordered = True