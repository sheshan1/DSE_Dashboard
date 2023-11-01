import csv
from flaskblog import db, create_app
from datetime import datetime
from flaskblog.models import AverageForClusters

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    # Use raw string or forward slashes in the file path
    file_path = r'D:/Downloads/Project/Final/average_values_for_clusters.csv'

    # Read data from CSV and insert into database
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            cluster = int(row['cluster'])
            speed = float(row['speed'])
            acceleration = float(row['acceleration'])
            radial_acceleration = float(row['radial_acceleration'])
            acceleration_der = float(row['acceleration_der'])

            avg = AverageForClusters(
                cluster=cluster,
                speed=speed,
                acceleration=acceleration,
                radial_acceleration=radial_acceleration,
                acceleration_der=acceleration_der
            )

            db.session.add(avg)

        db.session.commit()
