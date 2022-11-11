from init import db, ma

class Climber(db.Model):
    __tablename__= "climbers"
    # Created table attributes using imported db object
    climber_id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean(), default=False)
    user_name = db.Column(db.String(100))
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(80))
    email_address = db.Column(db.String, nullable=False, unique=True)
    created = db.Column(db.Date)

    ascents = db.relationship("Ascent", back_populates = "climber", cascade="all, delete")


class ClimberSchema(ma.Schema):

    # ascents = fields.List(fields.Nested("AscentSchema", exclude=["problem_id", "problem"]))

    class Meta:
    # Fields to expose
        fields = ("climber_id", "user_name", "password", "first_name", "last_name", 
        "email_address")
        dump = ("user_name", "email_address")
        ordered = True

class AdminClimberSchema(ma.Schema):
        fields = ("climber_id", "user_name", "password", "first_name", "last_name", 
        "email_address")
