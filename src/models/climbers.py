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