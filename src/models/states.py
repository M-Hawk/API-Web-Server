from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class State(db.Model):
    __tablename__= "states"
    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50), nullable=False)
    state_acronym = db.Column(db.String(10), nullable=False)
    created = db.Column(db.Date)

    areas = db.relationship("Area", back_populates="state", cascade="all, delete")

class StateSchema(ma.Schema):

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
        fields = ("state_id", "state_name", "state_acronym", "areas")
        ordered = True



