from flask import Blueprint, jsonify
from flaskblog.models import BusStop, BusData
from flask_apscheduler import APScheduler
import time

routes = Blueprint('routes', __name__)

last_id = 0  # Initialize with 0

@routes.route('/get_data')
def get_data():
    global last_id

    while True:
        data = BusData.query.filter(BusData.id > last_id).first()

        if data:
            data_dict = {
                'id': data.id,
                'deviceid': data.deviceid,
                'latitude': data.latitude,
                'longitude': data.longitude,
                'speed': data.speed,
                'date': data.date,
                'time': str(data.time),
                'geometry': data.geometry,
                'bus_stop': data.bus_stop,
                'trip_id': data.trip_id,
                'direction': data.direction,
                'acceleration': data.acceleration,
                'radial_acceleration': data.radial_acceleration,
                'distance': data.distance,
                # Add other fields as needed
            }

            last_id = data.id
            return jsonify(data=data_dict)

        time.sleep(3)


@routes.route("/map", methods=['GET'])
def get_busstops():
    all_bus_stops = BusStop.query.all()
    result = BusStop.bus_stops_schema.dump(all_bus_stops)
    return jsonify(result)
