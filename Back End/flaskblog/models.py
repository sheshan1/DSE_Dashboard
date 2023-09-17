from datetime import datetime
from flaskblog import db

class BusStop(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stop_id = db.Column(db.String(255))
    route_id = db.Column(db.Integer)
    direction = db.Column(db.String(255))
    address = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
