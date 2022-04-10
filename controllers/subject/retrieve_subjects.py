import json

from flask import jsonify
from bson.json_util import dumps

from . import subject_blueprint
from ...configurations.database import mongo

@subject_blueprint.route("/retrieve-subjects", methods=["GET"])
def retrieve_subjects():
    subjects = mongo.db.subject.find({
        "record_status": "ACTIVE",
    })

    if subjects:
        subjects = json.loads(dumps(subjects))
        subjects.reverse()

        return jsonify({
            "status": "200",
            "message": "subjects_retrieved_ok",
            "data": subjects
        })

    else:
        return jsonify({
            "status": "404",
            "message": "subjects_not_found",
            "data": []
        })