from datetime import datetime
from flask import jsonify
from flaskblog import db, ma


class BusStopSchema(ma.Schema):
    class Meta:
        fields = ('id', 'stop_id', 'route_id', 'direction', 'address', 'latitude', 'longitude')
        
class BusStop(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stop_id = db.Column(db.String(255))
    route_id = db.Column(db.Integer)
    direction = db.Column(db.String(255))
    address = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, stop_id, route_id, direction, address, latitude, longitude):
        self.stop_id = stop_id
        self.route_id = route_id
        self.direction = direction
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    bus_stop_schema = BusStopSchema()
    bus_stops_schema = BusStopSchema(many=True)

class BusDataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'deviceid', 'latitude', 'longitude', 'speed', 'date', 'time', 'geometry', 'bus_stop', 'trip_id', 'direction', 'acceleration', 'radial_acceleration', 'distance')

class BusData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deviceid = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    speed = db.Column(db.Float)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    geometry = db.Column(db.String(255))
    bus_stop = db.Column(db.String(255))
    trip_id = db.Column(db.Integer)
    direction = db.Column(db.String(255))
    acceleration = db.Column(db.Float)
    radial_acceleration = db.Column(db.Float)
    distance = db.Column(db.Float)

    def __init__(self, deviceid, latitude, longitude, speed, date, time, geometry, bus_stop, trip_id, direction, acceleration, radial_acceleration, distance):
        self.deviceid = deviceid
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.date = date
        self.time = time
        self.geometry = geometry
        self.bus_stop = bus_stop
        self.trip_id = trip_id
        self.direction = direction
        self.acceleration = acceleration
        self.radial_acceleration = radial_acceleration
        self.distance = distance

    bus_data_schema = BusDataSchema()
    bus_datas_schema = BusDataSchema(many=True)

