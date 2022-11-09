from init import db, ma

class State(db.Model):
    __tablename__= "states"
    # Created table attributes using imported db object
    state_id = db.Column(db.Integer, primary_key=True)
    # varchar (create tuples of state names)
    state_name = db.Column(db.String(50))


#create the State Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class StateSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("state_id", "state_name")


