from flask import Blueprint, jsonify

topic_blueprint = Blueprint("topic_blueprint", __name__)

from . import create_topic
from . import retrieve_topics
from . import retrieve_subject_topics
# from . import update_topic
# from . import delete_topic