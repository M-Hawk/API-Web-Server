from init import db, ma

class Ascent(db.Model):
    __tablename__= "ascents"
    # Created table attributes using imported db object
    ascent_id = db.Column(db.Integer, primary_key=True)
    tick_type = db.Column(db.String(50)) # varchar (create tuples of tick types)
    comments = db.Column(db.Text)
    created = db.Column(db.Date)

    climber_id = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey("problems.problem_id"), nullable=False)