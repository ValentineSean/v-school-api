import json

from flask import jsonify
from bson.json_util import dumps

from . import topic_blueprint
from ...configurations.database import mongo

@topic_blueprint.route("/retrieve-topics", methods=["GET"])
def retrieve_topics():
    topics = mongo.db.topic.find({
        "record_status": "ACTIVE",
    })

    if topics:
        topics = json.loads(dumps(topics))
        topics.reverse()

        return jsonify({
            "status": "200",
            "message": "topics_retrieved_ok",
            "data": topics
        })

    else:
        return jsonify({
            "status": "404",
            "message": "topics_not_found",
            "data": []
        })