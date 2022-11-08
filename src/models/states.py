from main import db

class State(db.Model):
    __tablename__= "states"
    # Created table attributes using imported db object
    state_id = db.Column(db.Integer, primary_key=True)
    # varchar (create tuples of state names)
    state_name = db.Column(db.String(50)) 
    
