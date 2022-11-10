# from init import db, ma
# from marshmallow import fields

# class Ascent(db.Model):
#     __tablename__= "ascents"
#     # Created table attributes using imported db object
#     ascent_id = db.Column(db.Integer, primary_key=True)
#     tick_type = db.Column(db.String(50)) # varchar (create tuples of tick types)
#     comments = db.Column(db.Text)
#     created = db.Column(db.Date)

#     climber_id = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"), nullable=False)
#     problem_id = db.Column(db.Integer, db.ForeignKey("problems.problem_id"), nullable=False)

#     problem = db.relationship("Problem", back_populates="ascents")
#     climber = db.relationship("Climber", back_populates="ascent", cascade="all, delete")

# class AscentSchema(ma.Schema):

#     problem = fields.Nested("ProblemSchema", only=["problem_name"])
#     climber = fields.Nested("ClimberSchema", only=["user_name"])

#     class Meta:
#     # Fields to expose
#         fields = ("ascent_id", "climber_id", "problem_id", "problem", "climber", "tick_type", "comments", "created")
#         ordered = True