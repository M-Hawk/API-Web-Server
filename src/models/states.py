from init import db, ma

class State(db.Model):
    __tablename__= "states"
    # Created table attributes using imported db object
    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50))
    state_acronym = db.Column(db.String(10))
    created = db.Column(db.Date)

#create the State Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class StateSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("state_id", "state_name", "state_acronym", "created")
        ordered = True



