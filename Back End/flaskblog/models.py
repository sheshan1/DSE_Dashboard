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
    # def __repr__(self):
    #     return f"BusStop('{self.stop_id}', '{self.route_id}', '{self.direction}', '{self.address}', '{self.latitude}', '{self.longitude}')"





# @routes.route("./", methods=['GET'])
# def get_busstops():
#     all_bus_stops = BusStop.query.all()
#     result = BusStop.bus_stops_schema.dump(all_bus_stops)
#     return jsonify(result)

