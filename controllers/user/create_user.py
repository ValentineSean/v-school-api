import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

from . import user_blueprint
from ...configurations.database import mongo

@user_blueprint.route("/create-user", methods=["POST"])
def create_user():
    user = request.json

    first_name = user["first_name"]
    last_name = user["last_name"]
    email = user["email"]
    role = user["role"]
    password = user["password"]
    creation_date = datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")

    new_user_id = mongo.db.user.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "role": role,
        "password": password,
        "creation_date": creation_date,
        "record_status": "ACTIVE"
    }).inserted_id

    new_user = mongo.db.user.find_one(
        {
            "$and": [
                {"_id": ObjectId(new_user_id)},
                {"record_status": "ACTIVE"}
            ]
        },

        {
            "password": 0,
        }
    )

    if new_user:
        new_user = json.loads(dumps(new_user))

        return jsonify({
            "status": "200",
            "message": "user_created_ok",
            "data": new_user
        })

    else:

        return jsonify({
            "status": "404",
            "message": "user_created_not_found",
            "data": []
        })