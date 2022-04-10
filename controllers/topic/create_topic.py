import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import topic_blueprint
from ...configurations.database import mongo

@topic_blueprint.route("/create-topic", methods=["POST"])
def create_topic():
    topic = request.json

    subject_id = topic["subject_id"]
    topic_name = topic["topic_name"]
    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

    new_topic_id = mongo.db.topic.insert_one({
        "subject_id": subject_id,
        "topic_name": topic_name,
        "upload_status": "no_media",
        "creation_date": creation_date,
        "record_status": "ACTIVE"
    }).inserted_id

    new_topic = mongo.db.topic.find_one({
        "$and": [
            {"_id": ObjectId(new_topic_id)},
            {"record_status": "ACTIVE"}
        ]
    })

    if new_topic:
        new_topic = json.loads(dumps(new_topic))

        return jsonify({
            "status": "200",
            "message": "topic_created_ok",
            "data": new_topic
        })

    else:

        return jsonify({
            "status": "404",
            "message": "topic_created_not_found",
            "data": []
        })