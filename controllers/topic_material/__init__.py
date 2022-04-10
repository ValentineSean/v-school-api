from flask import Blueprint, jsonify

topic_material_blueprint = Blueprint("topic_material_blueprint", __name__)

from . import upload_material
from . import retrieve_material