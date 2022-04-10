import json

from flask import jsonify
from bson.objectid import ObjectId
from bson.json_util import dumps

from . import topic_blueprint
from ...configurations.database import mongo

@topic_blueprint.route("/retrieve-subject-topics/<subject_id>", methods=["GET"])
def retrieve_subject_topics(subject_id):
    subject_topics = mongo.db.topic.find({
        "$and":[
            {
                "subject_id": subject_id
            },
            {
                "record_status": "ACTIVE",
            }
        ]
    })

    if subject_topics:
        subject_topics = json.loads(dumps(subject_topics))
        subject_topics.reverse()

        return jsonify({
            "status": "200",
            "message": "subject_topics_retrieved_ok",
            "data": subject_topics
        })

    else:
        return jsonify({
            "status": "404",
            "message": "subject_topics_not_found",
            "data": []
        })