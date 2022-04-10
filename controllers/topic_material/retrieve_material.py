from flask import jsonify

from . import topic_material_blueprint

@topic_material_blueprint.route("/retrieve-material", methods=["GET"])
def retrieve_material():
    return jsonify({
        "message": "retrieve material"
    })