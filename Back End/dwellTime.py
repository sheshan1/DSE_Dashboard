import csv
from flaskblog import db, create_app
from datetime import datetime
from flaskblog.models import DwellTime

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    file_path = r'D:/Downloads/Project/Final/df_for_dwelltime_model_updated.csv'

    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            trip_id = int(row['trip_id'])
            deviceid = int(row['deviceid'])
            direction = int(row['direction'])
            bus_stop = int(row['bus_stop'])
            dwell_time_in_seconds = int(row['dwell_time_in_seconds'])
            day_of_week = int(row['day_of_week'])
            time_of_day = float(row['time_of_day'])
            Sunday_holiday = int(row['Sunday/holiday'])
            saturday = int(row['saturday'])
            weekday_end = int(row['weekday/end'])
            week_no = int(row['week_no'])
            dt_w_1 = int(row['dt(w-1)'])
            dt_w_2 = int(row['dt(w-2)'])
            dt_w_3 = int(row['dt(w-3)'])
            dt_t_1 = int(row['dt(t-1)'])
            dt_t_2 = int(row['dt(t-2)'])
            dt_n_1 = int(row['dt(n-1)'])
            dt_n_2 = int(row['dt(n-2)'])
            dt_n_3 = int(row['dt(n-3)'])
            day = int(row['day'])
            month = int(row['month'])
            temp = float(row['temp'])
            precip = float(row['precip'])
            windspeed = float(row['windspeed'])
            conditions = int(row['conditions'])
            rt_n_1 = float(row['rt(n-1)'])
            stop_type = int(row['stop_type'])
            year = int(row['year'])
            arrival_hour = int(row['arrival_hour'])
            arrival_min = int(row['arrival_min'])
            arrival_sec = int(row['arrival_sec'])

            bus_stop = DwellTime(
                trip_id=trip_id,
                deviceid=deviceid,
                direction=direction,
                bus_stop=bus_stop,
                dwell_time_in_seconds=dwell_time_in_seconds,
                day_of_week=day_of_week,
                time_of_day=time_of_day,
                Sunday_holiday=Sunday_holiday,
                saturday=saturday,
                weekday_end=weekday_end,
                week_no=week_no,
                dt_w_1=dt_w_1,
                dt_w_2=dt_w_2,
                dt_w_3=dt_w_3,
                dt_t_1=dt_t_1,
                dt_t_2=dt_t_2,
                dt_n_1=dt_n_1,
                dt_n_2=dt_n_2,
                dt_n_3=dt_n_3,
                day=day,
                month=month,
                temp=temp,
                precip=precip,
                windspeed=windspeed,
                conditions=conditions,
                rt_n_1=rt_n_1,
                year=year,
                stop_type=stop_type,
                arrival_hour=arrival_hour,
                arrival_min=arrival_min,
                arrival_sec=arrival_sec
            )

            db.session.add(bus_stop)

        db.session.commit()
