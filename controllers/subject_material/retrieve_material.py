from flask import jsonify

from . import subject_material_blueprint

@subject_material_blueprint.route("/retrieve-material", methods=["GET"])
def retrieve_material():
    return jsonify({
        "message": "retrieve material"
    })