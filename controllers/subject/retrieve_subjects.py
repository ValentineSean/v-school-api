from flask import jsonify

from . import subject_blueprint

@subject_blueprint.route("/retrieve-subjects", methods=["GET"])
def retrieve_subjects():
    return jsonify({
        "message": "retrieve subjects"
    })