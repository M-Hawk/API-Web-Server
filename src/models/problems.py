from main import db

class Problem(db.Model):
    __tablename__= "problems"
    # Created table attributes using imported db object
    problem_id = db.Column(db.Integer, primary_key=True)
    area_id = db.Column(db.Integer, db.ForeignKey("areas.area_id"), nullable=False)
    problem_name = db.Column(db.String(50))
    grade = db.Column(db.String(4)) # Either add list of tuples or ensure V interpolated in front
    surface_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    access = db.Column(db.Text)
    height_metres = db.Column(db.Integer)
    comments = db.Column(db.Text)
    created = db.Column(db.Date)
    modified = db.Column(db.Date)