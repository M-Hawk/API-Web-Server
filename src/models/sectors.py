from init import db, ma

class Sector(db.Model):
    __tablename__= "sectors"
    # Created table attributes using imported db object
    sector_id = db.Column(db.Integer, primary_key=True)
    sector_name = db.Column(db.String(50)) # varchar
    description = db.Column(db.Text)
    access = db.Column(db.Text)
    latitude = db.Column(db.Float(precision=6))
    longitude = db.Column(db.Float(precision=6))
    created = db.Column(db.Date)

    area_id = db.Column(db.Integer, db.ForeignKey("areas.area_id"), nullable=False)


    # class AreaSchema(ma.Schema):
    #     class Meta:
    #     # Fields to expose
    #         fields = ("area_id", "area_name", "state", "description", "ethics", "access", 
    #         "latitude", "longitude", "created")
    #         ordered = True    