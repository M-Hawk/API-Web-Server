from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class State(db.Model):
    __tablename__= "states"
    # Created table attributes using imported db object
    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50), nullable=False)
    state_acronym = db.Column(db.String(10), nullable=False)
    created = db.Column(db.Date)

    # creates a relationship from states to areas when requests are sent, if the state is deleted so is the area within it
    areas = db.relationship("Area", back_populates="state", cascade="all, delete")

#create the State Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class StateSchema(ma.Schema):

    # allows areas to be JSON serializable when get request is sent for states list
    areas = fields.List(fields.Nested("AreaSchema", exclude=["state_id", "sectors"]))

    state_name = fields.String(required=True, validate=And(
        Length(min=2, max=100, error="State Name must be at least 2 characters long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))

    state_acronym = fields.String(required=True, validate=And(
        Length(min=1, max=100, error="State Acronym must be at least 1 characters long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))

    class Meta:
        # Fields to expose
        fields = ("state_id", "state_name", "state_acronym", "areas")
        ordered = True



