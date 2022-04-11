import json

from flask import jsonify
from bson.json_util import dumps

from . import user_blueprint
from ...configurations.database import mongo

@user_blueprint.route("/retrieve-users", methods=["GET"])
def retrieve_users():
    users = mongo.db.user.find(
        {
            "record_status": "ACTIVE",
        },
        {
            "password": 0,
        }
    )

    if users:
        users = json.loads(dumps(users))
        users.reverse()

        return jsonify({
            "status": "200",
            "message": "users_retrieved_ok",
            "data": users
        })

    else:
        return jsonify({
            "status": "404",
            "message": "users_not_found",
            "data": []
        })