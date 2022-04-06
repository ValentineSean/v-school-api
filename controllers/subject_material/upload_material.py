from flask import jsonify

from . import subject_material_blueprint

@subject_material_blueprint.route("/upload-material", methods=["POST"])
def upload_material():
    return jsonify({
        "message": "upload material"
    })