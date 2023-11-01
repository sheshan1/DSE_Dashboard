from flask import Blueprint, jsonify
from flaskblog.models import BusStop, Combined
import time
from datetime import datetime, timedelta
import threading
from sqlalchemy import func

routes = Blueprint('routes', __name__)

last_id = 0  # Initialize with 0

# Create a dictionary to store data by device_id
stored_data = {}
stop_data = {}

current_date = '2022-10-13'
current_time = '07:26:00'

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

@routes.route('/get_currentTime', methods=['GET'])
def get_currentTime():
    global current_time
    return jsonify({'current_time': current_time})

@routes.route('/get_matching_data', methods=['GET'])
def get_matching_data():
    global stored_data

    data_list = Combined.query.filter(
        Combined.date == current_date,
        Combined.time == current_time
    ).all()
    result = Combined.bus_datas_schema.dump(data_list)

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

@routes.route('/get_normCluster/<string:deviceid>', methods=['GET', 'POST'])
def get_normCluster(deviceid):
    global stored_data

    trip_id = stored_data[deviceid]['trip_id']
    segment = stored_data[deviceid]['segment']
    data = Combined.query.with_entities(Combined.segment, Combined.norm_cluster).filter(
        Combined.trip_id == trip_id,
        Combined.segment <= segment,
        Combined.norm_cluster >= 0
    ).order_by(Combined.segment.asc()).distinct().all()
    result = Combined.bus_datas_schema.dump(data)
    return jsonify(result)

@routes.route('/get_busstop/<string:deviceid>', methods=['GET', 'POST'])
def get_busstop(deviceid):
    global stored_data
    global stop_data

    segment = stored_data[deviceid]['segment']
    if segment > 0 and segment < 15:
        bus_stop = BusStop.query.filter_by(stop_id=str(segment+100)).first()
        stop_data[deviceid] = bus_stop.address
    elif segment == 15:
        bus_stop = 'Digana'
        stop_data[deviceid] = bus_stop
    else:
        if deviceid not in stop_data:
            return jsonify({'bus_stop': 'Next'})
    return jsonify({'bus_stop': stop_data[deviceid]})
    
@routes.route('/get_avgSpeed', methods=['GET'])
def get_avgSpeed():
    # calculate avg speed foe each segment and round to near 3 floating places
    avg_speed = Combined.query.with_entities(Combined.segment, func.round(func.avg(Combined.speed), 3).label('avg_speed')).group_by(Combined.segment).order_by(Combined.segment.asc()).all()
    # convert to list of dictionaries
    result = []
    for speed in avg_speed:
        result.append({'segment': speed[0], 'avg_speed': speed[1]})
    return jsonify(result)