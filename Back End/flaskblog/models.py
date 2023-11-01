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
        fields = ('id', 'deviceid', 'latitude', 'longitude', 'speed', 'date', 'time', 'bus_stop', 'trip_id', 'direction', 'acceleration', 'radial_acceleration', 'distance','segment')

class BusData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deviceid = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    speed = db.Column(db.Float)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    bus_stop = db.Column(db.String(255))
    trip_id = db.Column(db.Integer)
    direction = db.Column(db.String(255))
    acceleration = db.Column(db.Float)
    radial_acceleration = db.Column(db.Float)
    distance = db.Column(db.Float)
    segment = db.Column(db.Integer)

    def __init__(self, deviceid, latitude, longitude, speed, date, time, bus_stop, trip_id, direction, acceleration, radial_acceleration, distance, segment):
        self.deviceid = deviceid
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.date = date
        self.time = time
        self.bus_stop = bus_stop
        self.trip_id = trip_id
        self.direction = direction
        self.acceleration = acceleration
        self.radial_acceleration = radial_acceleration
        self.distance = distance
        self.segment = segment

    bus_data_schema = BusDataSchema()
    bus_datas_schema = BusDataSchema(many=True)

class RunningTimeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'trip_id', 'deviceid', 'direction', 'segment',
       'length', 'day_of_week', 'time_of_day', 'Sunday/holiday', 'saturday',
       'weekday/end', 'week_no', 'rt(w-1)', 'rt(w-2)', 'rt(w-3)', 'rt(t-1)',
       'rt(t-2)', 'rt(n-1)', 'rt(n-2)', 'rt(n-3)', 'hour_of_day', 'day',
       'month', 'temp', 'precip', 'windspeed', 'dt(n-1)', 'norm_cluster',
       'Cluster_0.0', 'Cluster_1.0', 'Cluster_2.0', 'year',
       'conditions_encoded', 'start_float', 'dayparts', 'speed',
       'acceleration', 'radial_acceleration', 'throttle_count', 'break_count',
       'cluster_in_1_segment_before', 'cluster_in_2_segment_before',
       'cluster_in_3_segment_before', 'speed_1_segment_before',
       'last_trip_cluster', 'norm_cluster_mode')
        
class RunningTime(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trip_id = db.Column(db.Integer)
    deviceid = db.Column(db.Integer)
    direction = db.Column(db.Integer)
    segment = db.Column(db.Integer)
    length = db.Column(db.Float)
    day_of_week = db.Column(db.Integer)
    time_of_day = db.Column(db.Float)
    Sunday_holiday = db.Column(db.Integer)
    saturday = db.Column(db.Integer)
    weekday_end = db.Column(db.Integer)
    week_no = db.Column(db.Integer)
    rt_w_1 = db.Column(db.Integer)
    rt_w_2 = db.Column(db.Integer)
    rt_w_3 = db.Column(db.Integer)
    rt_t_1 = db.Column(db.Integer)
    rt_t_2 = db.Column(db.Integer)
    rt_n_1 = db.Column(db.Integer)
    rt_n_2 = db.Column(db.Integer)
    rt_n_3 = db.Column(db.Integer)
    hour_of_day = db.Column(db.Integer)
    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    temp = db.Column(db.Float)
    precip = db.Column(db.Float)
    windspeed = db.Column(db.Float)
    dt_n_1 = db.Column(db.Integer)
    norm_cluster = db.Column(db.Integer)
    Cluster_0_0 = db.Column(db.Integer)
    Cluster_1_0 = db.Column(db.Integer)
    Cluster_2_0 = db.Column(db.Integer)
    year = db.Column(db.Integer)
    conditions_encoded = db.Column(db.Integer)
    start_float = db.Column(db.Float)
    dayparts = db.Column(db.Integer)
    speed = db.Column(db.Float)
    acceleration = db.Column(db.Float)
    radial_acceleration = db.Column(db.Float)
    throttle_count = db.Column(db.Float)
    break_count = db.Column(db.Float)
    cluster_in_1_segment_before = db.Column(db.Float)
    cluster_in_2_segment_before = db.Column(db.Float)
    cluster_in_3_segment_before = db.Column(db.Float)
    speed_1_segment_before = db.Column(db.Float)
    last_trip_cluster = db.Column(db.Float)
    norm_cluster_mode = db.Column(db.Integer)

    def __init__(self, trip_id, deviceid, direction, segment, length, day_of_week, time_of_day, Sunday_holiday, saturday, weekday_end, week_no, rt_w_1, rt_w_2, rt_w_3, rt_t_1, rt_t_2, rt_n_1, rt_n_2, rt_n_3, hour_of_day, day, month, temp, precip, windspeed, dt_n_1, norm_cluster, Cluster_0_0, Cluster_1_0, Cluster_2_0, year, conditions_encoded, start_float, dayparts, speed, acceleration, radial_acceleration, throttle_count, break_count, cluster_in_1_segment_before, cluster_in_2_segment_before, cluster_in_3_segment_before, speed_1_segment_before, last_trip_cluster, norm_cluster_mode):
        self.trip_id = trip_id
        self.deviceid = deviceid
        self.direction = direction
        self.segment = segment
        self.length = length
        self.day_of_week = day_of_week
        self.time_of_day = time_of_day
        self.Sunday_holiday = Sunday_holiday
        self.saturday = saturday
        self.weekday_end = weekday_end
        self.week_no = week_no
        self.rt_w_1 = rt_w_1
        self.rt_w_2 = rt_w_2
        self.rt_w_3 = rt_w_3
        self.rt_t_1 = rt_t_1
        self.rt_t_2 = rt_t_2
        self.rt_n_1 = rt_n_1
        self.rt_n_2 = rt_n_2
        self.rt_n_3 = rt_n_3
        self.hour_of_day = hour_of_day
        self.day = day
        self.month = month
        self.temp = temp
        self.precip = precip
        self.windspeed = windspeed
        self.dt_n_1 = dt_n_1
        self.norm_cluster = norm_cluster
        self.Cluster_0_0 = Cluster_0_0
        self.Cluster_1_0 = Cluster_1_0
        self.Cluster_2_0 = Cluster_2_0
        self.year = year
        self.conditions_encoded = conditions_encoded
        self.start_float = start_float
        self.dayparts = dayparts
        self.speed = speed
        self.acceleration = acceleration
        self.radial_acceleration = radial_acceleration
        self.throttle_count = throttle_count
        self.break_count = break_count
        self.cluster_in_1_segment_before = cluster_in_1_segment_before
        self.cluster_in_2_segment_before = cluster_in_2_segment_before
        self.cluster_in_3_segment_before = cluster_in_3_segment_before
        self.speed_1_segment_before = speed_1_segment_before
        self.last_trip_cluster = last_trip_cluster
        self.norm_cluster_mode = norm_cluster_mode

    running_time_schema = RunningTimeSchema()
    running_times_schema = RunningTimeSchema(many=True)


class DwellTimeSchema(ma.Schema):
    class Meta:
        fields = ('trip_id', 'deviceid', 'direction', 'bus_stop', 'day_of_week',
       'time_of_day', 'Sunday/holiday', 'saturday', 'weekday/end', 'week_no',
       'dt(w-1)', 'dt(w-2)', 'dt(w-3)', 'dt(t-1)', 'dt(t-2)', 'dt(n-1)',
       'dt(n-2)', 'dt(n-3)', 'day', 'month', 'temp', 'precip', 'windspeed',
       'conditions', 'rt(n-1)', 'stop_type', 'year',
       'arrival_hour', 'arrival_min', 'arrival_sec')
        
class DwellTime(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trip_id = db.Column(db.Integer)
    deviceid = db.Column(db.Integer)
    direction = db.Column(db.Integer)
    bus_stop = db.Column(db.Integer)
    day_of_week = db.Column(db.Integer)
    time_of_day = db.Column(db.Float)
    Sunday_holiday = db.Column(db.Integer)
    saturday = db.Column(db.Integer)
    weekday_end = db.Column(db.Integer)
    week_no = db.Column(db.Integer)
    dt_w_1 = db.Column(db.Integer)
    dt_w_2 = db.Column(db.Integer)
    dt_w_3 = db.Column(db.Integer)
    dt_t_1 = db.Column(db.Integer)
    dt_t_2 = db.Column(db.Integer)
    dt_n_1 = db.Column(db.Integer)
    dt_n_2 = db.Column(db.Integer)
    dt_n_3 = db.Column(db.Integer)
    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    temp = db.Column(db.Float)
    precip = db.Column(db.Float)
    windspeed = db.Column(db.Float)
    conditions = db.Column(db.Integer)
    rt_n_1 = db.Column(db.Float)
    stop_type = db.Column(db.Integer)
    year = db.Column(db.Integer)
    arrival_hour = db.Column(db.Integer)
    arrival_min = db.Column(db.Integer)
    arrival_sec = db.Column(db.Integer)

    def __init__(self, trip_id, deviceid, direction, bus_stop, day_of_week, time_of_day, Sunday_holiday, saturday, weekday_end, week_no, dt_w_1, dt_w_2, dt_w_3, dt_t_1, dt_t_2, dt_n_1, dt_n_2, dt_n_3, day, month, temp, precip, windspeed, conditions, rt_n_1, stop_type, year, arrival_hour, arrival_min, arrival_sec):
        self.trip_id = trip_id
        self.deviceid = deviceid
        self.direction = direction
        self.bus_stop = bus_stop
        self.day_of_week = day_of_week
        self.time_of_day = time_of_day
        self.Sunday_holiday = Sunday_holiday
        self.saturday = saturday
        self.weekday_end = weekday_end
        self.week_no = week_no
        self.dt_w_2 = dt_w_2
        self.dt_w_1 = dt_w_1
        self.dt_w_3 = dt_w_3
        self.dt_t_1 = dt_t_1
        self.dt_t_2 = dt_t_2
        self.dt_n_1 = dt_n_1
        self.dt_n_2 = dt_n_2
        self.dt_n_3 = dt_n_3
        self.day = day
        self.month = month
        self.temp = temp
        self.precip = precip
        self.windspeed = windspeed
        self.rt_n_1 = rt_n_1
        self.year = year
        self.conditions = conditions
        self.stop_type = stop_type
        self.arrival_hour = arrival_hour
        self.arrival_min = arrival_min
        self.arrival_sec = arrival_sec

    dwell_time_schema = DwellTimeSchema()
    dwell_times_schema = DwellTimeSchema(many=True)

class PredictionsSchema(ma.Schema):
    class Meta:
        fields = ('trip_id', 'segment', 'run_time', 'start_bus_stop', 'end_bus_stop', 'dwell_time', 'arrival_time')
        
class Predictions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trip_id = db.Column(db.Integer)
    segment = db.Column(db.Integer)
    run_time = db.Column(db.Float)
    start_bus_stop = db.Column(db.String(255))
    end_bus_stop = db.Column(db.String(255))
    dwell_time = db.Column(db.Float)
    arrival_time = db.Column(db.Float)

    def __init__(self, trip_id, segment, run_time, start_bus_stop, end_bus_stop, dwell_time, arrival_time):
        self.trip_id = trip_id
        self.segment = segment
        self.run_time = run_time
        self.start_bus_stop = start_bus_stop
        self.end_bus_stop = end_bus_stop
        self.dwell_time = dwell_time
        self.arrival_time = arrival_time

    prediction_schema = PredictionsSchema()
    predictions_schema = PredictionsSchema(many=True)


class CombinedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'deviceid', 'latitude', 'longitude', 'speed', 'date', 'time', 'bus_stop', 'trip_id', 'direction', 'acceleration', 'radial_acceleration', 'distance','segment', 'arrival_time', 'predicted_time', 'norm_cluster')

class Combined(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deviceid = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    speed = db.Column(db.Float)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    bus_stop = db.Column(db.String(255))
    trip_id = db.Column(db.Integer)
    direction = db.Column(db.String(255))
    acceleration = db.Column(db.Float)
    radial_acceleration = db.Column(db.Float)
    distance = db.Column(db.Float)
    segment = db.Column(db.Integer)
    arrival_time = db.Column(db.Time)
    predicted_time = db.Column(db.Time)
    norm_cluster = db.Column(db.Integer)

    def __init__(self, deviceid, latitude, longitude, speed, date, time, bus_stop, trip_id, direction, acceleration, radial_acceleration, distance, segment, arrival_time, predicted_time, norm_cluster):
        self.deviceid = deviceid
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.date = date
        self.time = time
        self.bus_stop = bus_stop
        self.trip_id = trip_id
        self.direction = direction
        self.acceleration = acceleration
        self.radial_acceleration = radial_acceleration
        self.distance = distance
        self.segment = segment
        self.arrival_time = arrival_time
        self.predicted_time = predicted_time
        self.norm_cluster = norm_cluster

    bus_data_schema = CombinedSchema()
    bus_datas_schema = CombinedSchema(many=True)

class AverageForClusters(ma.Schema):
    class Meta:
        fields = ('id', 'cluster', 'speed', 'acceleration', 'radial_acceleration', 'acceleration_der')
        
class AverageForClusters(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cluster = db.Column(db.Integer)
    speed = db.Column(db.Float)
    acceleration = db.Column(db.Float)
    radial_acceleration = db.Column(db.Float)
    acceleration_der = db.Column(db.Float)

    def __init__(self, cluster, speed, acceleration, radial_acceleration, acceleration_der ):
        self.cluster = cluster
        self.speed = speed
        self.acceleration = acceleration
        self.radial_acceleration = radial_acceleration
        self.acceleration_der = acceleration_der

    avg_cluster = AverageForClusters()
    avgs_cluster = AverageForClusters(many=True)

class AvgPercentage(ma.Schema):
    class Meta:
        fields = ('id', 'deviceid', 'Cluster_0.0', 'Cluster_1.0', 'Cluster_2.0')
        
class AvgPercentage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deviceid = db.Column(db.Integer)
    Cluster_0 = db.Column(db.Integer)
    Cluster_1 = db.Column(db.Integer)
    Cluster_2 = db.Column(db.Integer)

    def __init__(self, deviceid, Cluster_0, Cluster_1, Cluster_2 ):
        self.deviceid = deviceid
        self.Cluster_0= Cluster_0
        self.Cluster_1 = Cluster_1
        self.Cluster_2 = Cluster_2

    avg_percentage = AvgPercentage()
    avgs_percentage = AvgPercentage(many=True)

