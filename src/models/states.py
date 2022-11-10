from init import db, ma
from marshmallow import fields

class State(db.Model):
    __tablename__= "states"
    # Created table attributes using imported db object
    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50))
    state_acronym = db.Column(db.String(10))
    created = db.Column(db.Date)

    # creates a relationship from states to areas when requests are sent, if the state is deleted so is the area within it
    areas = db.relationship("Area", back_populates="state", cascade="all, delete")

#create the State Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class StateSchema(ma.Schema):

    # allows areas to be JSON serializable when get request is sent for states list
    areas = fields.List(fields.Nested("AreaSchema", exclude=["state_id", "state"]))

    class Meta:
        # Fields to expose
        fields = ("state_id", "state_name", "state_acronym", "areas", "created")
        ordered = True



