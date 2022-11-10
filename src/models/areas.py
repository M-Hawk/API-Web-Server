from init import db, ma
from marshmallow import fields

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

class AreaSchema(ma.Schema):

    state = fields.Nested("StateSchema", only=["state_name"])

    class Meta:
    # Fields to expose
        fields = ("area_id", "area_name", "state_id", "state", "description", "ethics", "access", 
        "latitude", "longitude", "created")
        ordered = True