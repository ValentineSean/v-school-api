from flask import Blueprint, jsonify

auth_blueprint = Blueprint("auth_blueprint", __name__)

from . import login