from flask import jsonify

from . import subject_blueprint

@subject_blueprint.route("/delete-subject", methods=["DELETE"])
def delete_subject():
    return jsonify({
        "message": "delete subject"
    })