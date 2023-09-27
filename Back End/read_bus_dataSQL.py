import csv
from flaskblog import db, create_app
import datetime
from flaskblog.models import BusData

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    # Use raw string or forward slashes in the file path
    file_path = r'D:/Downloads/Compressed/DataOut/bus_data_SQL.csv'

    # Read data from CSV and insert into database
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            deviceid = row['deviceid']
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            speed = float(row['speed'])

            date_obj = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
            date = date_obj.date()
            # date = datetime.date(row['date'], '%Y-%m-%d')
            time_obj = datetime.datetime.strptime(row['time'], '%H:%M:%S')
            tiem = time_obj.time()
            # time = datetime.time(row['time'], '%H:%M:%S')

            geometry = row['geometry']
            bus_stop = row['bus_stop']
            trip_id = int(row['trip_id'])
            direction = row['direction']
            acceleration = float(row['acceleration'])
            radial_acceleration = float(row['radial_acceleration'])
            distance = float(row['distance_from_start'])
            

            bus_data = BusData(
                deviceid=row['deviceid'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                speed=row['speed'],
                date=row['date'],
                time=row['time'],
                geometry=row['geometry'],
                bus_stop=row['bus_stop'],
                trip_id=row['trip_id'],
                direction=row['direction'],
                acceleration=row['acceleration'],
                radial_acceleration=row['radial_acceleration'],
                distance=row['distance_from_start']
            )

            db.session.add(bus_data)

        db.session.commit()
