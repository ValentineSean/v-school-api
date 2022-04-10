import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import subject_blueprint
from ...configurations.database import mongo

@subject_blueprint.route("/create-subject", methods=["POST"])
def create_subject():
    subject = request.json

    subject_name = subject["subject_name"]
    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

    new_subject_id = mongo.db.subject.insert_one({
        "subject_name": subject_name,
        "creation_date": creation_date,
        "record_status": "ACTIVE"
    }).inserted_id

    new_subject = mongo.db.subject.find_one({
        "$and": [
            {"_id": ObjectId(new_subject_id)},
            {"record_status": "ACTIVE"}
        ]
    })

    if new_subject:
        new_subject = json.loads(dumps(new_subject))

        return jsonify({
            "status": "200",
            "message": "subject_created_ok",
            "data": new_subject
        })

    else:

        return jsonify({
            "status": "404",
            "message": "subject_created_not_found",
            "data": []
        })