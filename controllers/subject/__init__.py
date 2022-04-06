from flask import Blueprint, jsonify

subject_blueprint = Blueprint("subject_blueprint", __name__)

from . import create_subject
from . import retrieve_subjects
from . import update_subject
from . import delete_subject