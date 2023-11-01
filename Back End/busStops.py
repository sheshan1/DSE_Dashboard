import csv
from flaskblog import db, create_app
from datetime import datetime
from flaskblog.models import BusStop

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    # Use raw string or forward slashes in the file path
    file_path = r'D:/Downloads/Project/bus_stops_and_terminals_654.csv'

    # Read data from CSV and insert into database
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            stop_id = row['stop_id']
            route_id = int(row['route_id'])
            direction = row['direction']
            address = row['address']
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])

            bus_stop = BusStop(
                stop_id=stop_id,
                route_id=route_id,
                direction=direction,
                address=address,
                latitude=latitude,
                longitude=longitude
            )

            db.session.add(bus_stop)

        db.session.commit()
