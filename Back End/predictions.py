import csv
from flaskblog import db, create_app
from datetime import datetime
from flaskblog.models import Predictions

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    # Use raw string or forward slashes in the file path
    file_path = r'D:/Downloads/Project/Final/predictions.csv'

    # Read data from CSV and insert into database
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            trip_id = int(row['trip_id'])
            segment = int(row['segment'])
            run_time = float(row['predicted_run_time_with_features'])
            start_bus_stop = row['start_bus_stop']
            end_bus_stop = row['end_bus_stop']
            dwell_time = float(row['predicted_dwel_time_with_features'])
            arrival_time = float(row['total_predicted_arrival_time_with_features'])

            predictions = Predictions(
                trip_id=trip_id,
                segment=segment,
                run_time=run_time,
                start_bus_stop=start_bus_stop,
                end_bus_stop=end_bus_stop,
                dwell_time=dwell_time,
                arrival_time=arrival_time
            )

            db.session.add(predictions)

        db.session.commit()
