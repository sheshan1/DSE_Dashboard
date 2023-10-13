from flask import Blueprint, jsonify
from flaskblog.models import BusStop, BusData
import time
from datetime import datetime, timedelta
import threading

routes = Blueprint('routes', __name__)

last_id = 0  # Initialize with 0

# Create a dictionary to store data by device_id
stored_data = {}

current_date = '2021-10-18'
current_time = '09:02:14'

def start_clock():
    global current_date, current_time

    while True:
        current_time = (datetime.strptime(current_time, '%H:%M:%S') + timedelta(seconds=1)).strftime('%H:%M:%S')
        if current_time == '00:00:00':
            current_date = (datetime.strptime(current_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
            current_time = '00:00:01'
        time.sleep(1)

clock_thread = threading.Thread(target=start_clock)
clock_thread.start()

@routes.route('/get_matching_data', methods=['GET'])
def get_matching_data():
    global stored_data

    data_list = BusData.query.filter(
        BusData.date == current_date,
        BusData.time == current_time
    ).all()
    result = BusData.bus_datas_schema.dump(data_list)

    for data in result:
        stored_data[data['deviceid']] = data

    # Convert the dictionary to a list of values
    unique_data = list(stored_data.values())

    return jsonify(unique_data)

@routes.route('/get_data/<string:deviceid>', methods=['GET', 'POST'])
def get_data(deviceid):
    global stored_data
    return jsonify(stored_data[deviceid])

@routes.route("/map", methods=['GET'])
def get_busstops():
    all_bus_stops = BusStop.query.all()
    result = BusStop.bus_stops_schema.dump(all_bus_stops)
    return jsonify(result)

@routes.route('/get_deviceids', methods=['GET'])
def get_deviceids():
    global stored_data
    unique_deviceids = sorted(list(stored_data.keys()))
    return jsonify(unique_deviceids)
