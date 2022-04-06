from flask import jsonify

from . import subject_blueprint

@subject_blueprint.route("/update-subject", methods=["PUT"])
def update_subject():
    return jsonify({
        "message": "update subject"
    })