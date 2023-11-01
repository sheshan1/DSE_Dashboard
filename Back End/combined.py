import csv
from flaskblog import db, create_app
import datetime
from flaskblog.models import Combined

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    # Use raw string or forward slashes in the file path
    file_path = r'D:/Downloads/Project/Final/combined_3.csv'

    # Read data from CSV and insert into database
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            deviceid = int(row['deviceid'])
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            speed = float(row['speed'])
            date_obj = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
            date = date_obj.date()
            time_obj = datetime.datetime.strptime(row['time'], '%H:%M:%S')
            time = time_obj.time()
            bus_stop = row['bus_stop']
            trip_id = int(row['trip_id'])
            direction = row['direction']
            acceleration = float(row['acceleration'])
            radial_acceleration = float(row['radial_acceleration'])
            distance = float(row['distance_from_start'])
            segment = int(row['segment'])
            time_obj = datetime.datetime.strptime(row['arrival_time'], '%H:%M:%S')
            arrival_time = time_obj.time()
            time_obj = datetime.datetime.strptime(row['predicted_time'], '%H:%M:%S')
            predicted_time = time_obj.time()
            norm_cluster = int(row['norm_cluster'])

            bus_data = Combined(
                deviceid=deviceid,
                latitude=latitude,
                longitude=longitude,
                speed=speed,
                date=date,
                time=time,
                bus_stop=bus_stop,
                trip_id=trip_id,
                direction=direction,
                acceleration=acceleration,
                radial_acceleration=radial_acceleration,
                distance=distance,
                segment=segment,
                arrival_time=arrival_time,
                predicted_time=predicted_time,
                norm_cluster=norm_cluster
            )

            db.session.add(bus_data)

        db.session.commit()
