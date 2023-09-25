from flask import Blueprint, jsonify
# from flask_login import current_user, login_required
# from flaskblog import db
from flaskblog.models import BusStop

routes = Blueprint('routes', __name__)

@routes.route("/map", methods=['GET'])
def get_busstops():
    all_bus_stops = BusStop.query.all()
    result = BusStop.bus_stops_schema.dump(all_bus_stops)
    return jsonify(result)

