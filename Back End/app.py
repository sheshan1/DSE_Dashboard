# # from flask import Flask, jsonify, request 
# # from flask_sqlalchemy import SQLAlchemy
# # import datetime
# # from flask_marshmallow import Marshmallow
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sheshan@localhost:3306/database'
# # app.config['SQLALCHEMY_TRACK_MODIFICATINOS'] = False

# # db = SQLAlchemy(app)
# # ma = Marshmallow(app)

# # class BusStop(db.Model):
# #     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     stop_id = db.Column(db.String(255))
# #     route_id = db.Column(db.Integer)
# #     direction = db.Column(db.String(255))
# #     address = db.Column(db.String(255))
# #     latitude = db.Column(db.Float)
# #     longitude = db.Column(db.Float)

# #     def __init__(self, stop_id, route_id, direction, address, latitude, longitude):
# #         self.stop_id = stop_id
# #         self.route_id = route_id
# #         self.direction = direction
# #         self.address = address
# #         self.latitude = latitude
# #         self.longitude = longitude

# #     def __repr__(self):
# #         return f"BusStop('{self.stop_id}', '{self.route_id}', '{self.direction}', '{self.address}', '{self.latitude}', '{self.longitude}')"

# # class BusStopSchema(ma.Schema):
# #     class Meta:
# #         fields = ('id', 'stop_id', 'route_id', 'direction', 'address', 'latitude', 'longitude')

# # bus_stop_schema = BusStopSchema()
# # bus_stops_schema = BusStopSchema(many=True)

# # @app.route("/get", methods=['GET'])
# # def get_busstops():
# #     all_bus_stops = BusStop.query.all()
# #     result = BusStop.bus_stops_schema.dump(all_bus_stops)
# #     return jsonify(result)

# # if __name__ == "__main__":
# #     app.run(debug=True)

# from flask import Flask, jsonify, request 
# from flask_sqlalchemy import SQLAlchemy
# import datetime
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sheshan@localhost:3306/database'
# app.config['SQLALCHEMY_TRACK_MODIFICATINOS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)


# class BusStop(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     stop_id = db.Column(db.String(255))
#     route_id = db.Column(db.Integer)
#     direction = db.Column(db.String(255))
#     address = db.Column(db.String(255))
#     latitude = db.Column(db.Float)
#     longitude = db.Column(db.Float)

#     def __init__(self, stop_id, route_id, direction, address, latitude, longitude):
#         self.stop_id = stop_id
#         self.route_id = route_id
#         self.direction = direction
#         self.address = address
#         self.latitude = latitude
#         self.longitude = longitude

# class BusStopSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'stop_id', 'route_id', 'direction', 'address', 'latitude', 'longitude')

# bus_stop_schema = BusStopSchema()
# bus_stops_schema = BusStopSchema(many=True)

# @app.route('/map', methods = ['GET'])
# def get_busstops():
#     all_articles = BusStop.query.all()
#     results = bus_stops_schema.dump(all_articles)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)
 