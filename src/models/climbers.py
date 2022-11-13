from init import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf, Length, And, Regexp 

class Climber(db.Model):
    __tablename__= "climbers"
    climber_id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean(), default=False)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email_address = db.Column(db.String, nullable=False, unique=True)
    created = db.Column(db.Date)

    ascents = db.relationship("Ascent", back_populates = "climber", cascade="all, delete")


class ClimberSchema(ma.Schema):

    ascents = fields.List(fields.Nested("AscentSchema", exclude=["climber"]))

    email_address = fields.String(required=True, validate=And(
        Length(min=1, error="Email Address must be at least 1 characters long"),
        Regexp("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", error="Please enter a valid email address")
    ))
    user_name = fields.String(required=True, validate=And(
        Length(min=4, max=100, error="User Name must be at least 4 characters long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))
    password = fields.String(required=True, validate=And(
        Length(min=8, error="Password must be at least 8 characters long and preferably contain letters and numbers"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))
    first_name = fields.String(required=True, validate=And(
        Length(min=1,  max=50, error="First Name must be at least 1 character long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))
    last_name = fields.String(required=True, validate=And(
        Length(min=1, max=80, error="Last Name must be at least 1 character long"),
        Regexp("^[a-zA-Z0-9 ]+$", error="Only letters, numbers and spaces are allowed")
    ))

    class Meta:
        fields = ("climber_id", "admin", "user_name", "password", "first_name", "last_name", 
        "email_address", "ascents")
        ordered = True

