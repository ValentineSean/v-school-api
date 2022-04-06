from flask import jsonify

from . import subject_blueprint

@subject_blueprint.route("/create-subject", methods=["POST"])
def create_subject():
    return jsonify({
        "message": "create subject"
    })