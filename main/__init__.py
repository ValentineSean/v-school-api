from flask import Flask, jsonify
from flask_cors import CORS

# Configurations
from ..configurations.database import mongo
from ..configurations.database import database_credentials

# Blueprints
from ..controllers.subject_material import subject_material_blueprint
from ..controllers.subject import subject_blueprint

app = Flask(__name__)

CORS(app)

app.config["MONGO_URI"] = "mongodb://{}/{}".format(
    database_credentials["host"],
    database_credentials["database"]
)

mongo.init_app(app)

def create_app():
    app.register_blueprint(subject_material_blueprint)
    app.register_blueprint(subject_blueprint)

    return app

app = create_app()