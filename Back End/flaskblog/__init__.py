from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flaskblog.config import config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from flaskblog import models  # Importing models here to avoid circular imports
        db.create_all()

    return app
