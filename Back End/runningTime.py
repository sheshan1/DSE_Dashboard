import csv
from flaskblog import db, create_app
from datetime import datetime
from flaskblog.models import RunningTime

# Initialize the Flask app and SQLAlchemy
app = create_app()
with app.app_context():
    db.create_all()

    file_path = r'D:/Downloads/Project/Final/df_for_running_time_model_updated.csv'

    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            trip_id = int(row['trip_id'])
            deviceid = int(row['deviceid'])
            direction = int(row['direction'])
            segment = int(row['segment'])
            run_time_in_seconds = int(row['run_time_in_seconds'])
            length = float(row['length'])
            day_of_week = int(row['day_of_week'])
            time_of_day = float(row['time_of_day'])
            Sunday_holiday = int(row['Sunday/holiday'])
            saturday = int(row['saturday'])
            weekday_end = int(row['weekday/end'])
            week_no = int(row['week_no'])
            rt_w_1 = int(row['rt(w-1)'])
            rt_w_2 = int(row['rt(w-2)'])
            rt_w_3 = int(row['rt(w-3)'])
            rt_t_1 = int(row['rt(t-1)'])
            rt_t_2 = int(row['rt(t-2)'])
            rt_n_1 = int(row['rt(n-1)'])
            rt_n_2 = int(row['rt(n-2)'])
            rt_n_3 = int(row['rt(n-3)'])
            hour_of_day = int(row['hour_of_day'])
            day = int(row['day'])
            month = int(row['month'])
            temp = float(row['temp'])
            precip = float(row['precip'])
            windspeed = float(row['windspeed'])
            dt_n_1 = int(row['dt(n-1)'])
            norm_cluster = int(row['norm_cluster'])
            Cluster_0_0 = int(row['Cluster_0.0'])
            Cluster_1_0 = int(row['Cluster_1.0'])
            Cluster_2_0 = int(row['Cluster_2.0'])
            year = int(row['year'])
            conditions_encoded = int(row['conditions_encoded'])
            start_float = float(row['start_float'])
            dayparts = int(row['dayparts'])
            speed = float(row['speed'])
            acceleration = float(row['acceleration'])
            radial_acceleration = float(row['radial_acceleration'])
            throttle_count = float(row['throttle_count'])
            break_count = float(row['break_count'])
            cluster_in_1_segment_before = float(row['cluster_in_1_segment_before']) if row['cluster_in_1_segment_before'] != '' else None
            cluster_in_2_segment_before = float(row['cluster_in_2_segment_before']) if row['cluster_in_2_segment_before'] != '' else None
            cluster_in_3_segment_before = float(row['cluster_in_3_segment_before']) if row['cluster_in_3_segment_before'] != '' else None
            # cluster_in_2_segment_before = row['cluster_in_2_segment_before']
            # cluster_in_3_segment_before = row['cluster_in_3_segment_before']
            speed_1_segment_before_value = row['speed_1_segment_before']
            speed_1_segment_before = float(speed_1_segment_before_value) if speed_1_segment_before_value and speed_1_segment_before_value.replace('.', '', 1).isdigit() else None

            # last_trip_cluster = row['last_trip_cluster']
            last_trip_cluster = float(row['last_trip_cluster']) if row['last_trip_cluster'] != '' else None

            norm_cluster_mode = int(row['norm_cluster_mode'])

            bus_stop = RunningTime(
                trip_id=trip_id,
                deviceid=deviceid,
                direction=direction,
                segment=segment,
                run_time_in_seconds=run_time_in_seconds,
                length=length,
                day_of_week=day_of_week,
                time_of_day=time_of_day,
                Sunday_holiday=Sunday_holiday,
                saturday=saturday,
                weekday_end=weekday_end,
                week_no=week_no,
                rt_w_1=rt_w_1,
                rt_w_2=rt_w_2,
                rt_w_3=rt_w_3,
                rt_t_1=rt_t_1,
                rt_t_2=rt_t_2,
                rt_n_1=rt_n_1,
                rt_n_2=rt_n_2,
                rt_n_3=rt_n_3,
                hour_of_day=hour_of_day,
                day=day,
                month=month,
                temp=temp,
                precip=precip,
                windspeed=windspeed,
                dt_n_1=dt_n_1,
                norm_cluster=norm_cluster,
                Cluster_0_0=Cluster_0_0,
                Cluster_1_0=Cluster_1_0,
                Cluster_2_0=Cluster_2_0,
                year=year,
                conditions_encoded=conditions_encoded,
                start_float=start_float,
                dayparts=dayparts,
                speed=speed,
                acceleration=acceleration,
                radial_acceleration=radial_acceleration,
                throttle_count=throttle_count,
                break_count=break_count,
                cluster_in_1_segment_before=cluster_in_1_segment_before,
                cluster_in_2_segment_before=cluster_in_2_segment_before,
                cluster_in_3_segment_before=cluster_in_3_segment_before,
                speed_1_segment_before=speed_1_segment_before,
                last_trip_cluster=last_trip_cluster,
                norm_cluster_mode=norm_cluster_mode
            )

            db.session.add(bus_stop)

        db.session.commit()
