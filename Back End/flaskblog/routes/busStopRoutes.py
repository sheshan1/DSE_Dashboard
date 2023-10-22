from flask import Blueprint, jsonify
from flaskblog.models import BusStop, BusData, DwellTime, RunningTime
import time
from datetime import datetime, timedelta
import threading
import joblib

routes = Blueprint('routes', __name__)

last_id = 0  # Initialize with 0

# Create a dictionary to store data by device_id
stored_data = {}

current_date = '2021-10-18'
current_time = '09:02:14'

dwelltime_model = joblib.load('flaskblog/models/dwelltime_model.sav')
runningtime_model = joblib.load('flaskblog/models/running_time_model.sav')

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

    for data in unique_data:
        if data['bus_stop'] != 0:  # Check if the bus is at a bus stop
            # Get the relevant features for prediction (e.g., feature1, feature2, ...)
            features = [data['feature1'], data['feature2'], ...]

            # Predict dwell time
            dwell_time_prediction = dwelltime_model.predict([features])

            # Predict running time
            running_time_prediction = runningtime_model.predict([features])

            # Add the predictions to the data
            data['dwell_time_prediction'] = dwell_time_prediction[0]  # Assuming single prediction
            data['running_time_prediction'] = running_time_prediction[0]  # Assuming single prediction

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

@routes.route('/get_dwelltime/<string:deviceid>', methods=['GET'])
def get_dwelltime(deviceid):
    global stored_data, dwelltime_model
    data = stored_data[deviceid]
    data['dwelltime'] = dwelltime_model.predict([[data['distance'], data['speed']]])[0]
    return jsonify(data)

@routes.route('/get_runningtime/<string:deviceid>', methods=['GET'])
def get_runningtime(deviceid):
    global stored_data, runningtime_model
    data = stored_data[deviceid]
    data['runningtime'] = runningtime_model.predict([[data['distance'], data['speed']]])[0]
    return jsonify(data)
