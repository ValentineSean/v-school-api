from flask import Blueprint, jsonify

subject_material_blueprint = Blueprint("subject_material_blueprint", __name__)

from . import upload_material
from . import retrieve_material