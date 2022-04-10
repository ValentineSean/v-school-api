import os
import json

from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
# from deepgram import Deepgram
# from dotenv import load_dotenv

from . import topic_material_blueprint
from ...configurations.database import mongo

from ...native_functions.deepgram_functions.generate_transcription import generate_transcription
from ...native_functions.dropbox_functions.upload_files import upload_files

# load_dotenv()

# deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

@topic_material_blueprint.route("/upload-material", methods=["POST"])
def upload_material():

    topic_id = request.form["topic_id"]
    audio_file = request.files["audio_file"]
    new_folder = topic_id

    # print(audio_file.filename)
    audio_file_name = "{}.mp3".format(new_folder)

    if audio_file_name != "":
        os.makedirs("media_files\\{}".format(new_folder))
        folder_path = "media_files\\{}".format(new_folder)
        audio_file_name = os.path.join(folder_path, audio_file_name)
        audio_file.save(audio_file_name)

        generate_transcription(audio_file_name, new_folder)

        shared_links = upload_files(new_folder)

        mongo.db.topic.update_one({
                "_id": ObjectId(topic_id),
            },

            {"$set": {
                "mp3_shared_link": shared_links["mp3_shared_link"],
                "vtt_shared_link": shared_links["vtt_shared_link"],
                "upload_status": "uploaded",
            }
        })

        updated_topic = mongo.db.topic.find_one({"_id": ObjectId(topic_id)})

        if updated_topic:
            updated_topic = json.loads(dumps(updated_topic))

            return jsonify({
                "status": "200",
                "message": "file_uploaded_ok",
                "data": updated_topic
            })

        else:
            return jsonify({
                "status": "404",
                "message": "file_uploaded_not_found",
                "data": {}
            })

    else:
        return jsonify({
            "status": "400",
            "message": "invalid_file_name",
            "data": {}
        })