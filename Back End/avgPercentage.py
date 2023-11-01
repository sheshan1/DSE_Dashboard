import csv
from flaskblog import db, create_app
from datetime import datetime
from flaskblog.models import AvgPercentage

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    # Use raw string or forward slashes in the file path
    file_path = r'D:/Downloads/Project/Final/average_cluster_percentage_per_device1.csv'

    # Read data from CSV and insert into database
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            deviceid = int(row['deviceid'])
            Cluster_0 = int(row['Cluster_0.0'])
            Cluster_1 = int(row['Cluster_1.0'])
            Cluster_2 = int(row['Cluster_2.0'])

            percentage = AvgPercentage(
                deviceid=deviceid,
                Cluster_0=Cluster_0,
                Cluster_1=Cluster_1,
                Cluster_2=Cluster_2
            )

            db.session.add(percentage)

        db.session.commit()
