import os

from flask import jsonify, request
# from deepgram import Deepgram
# from dotenv import load_dotenv

from . import subject_material_blueprint

from ...native_functions.deepgram_functions.generate_transcription import generate_transcription

# load_dotenv()

# deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

@subject_material_blueprint.route("/upload-material", methods=["POST"])
def upload_material():

    audio_file = request.files["audio_file"]

    # print(audio_file.filename)

    audio_file_name = audio_file.filename

    if audio_file_name != "":
        folder_path = "media_files"
        audio_file_name = os.path.join(folder_path, audio_file_name)
        audio_file.save(audio_file_name)

        generate_transcription(audio_file_name)

    else:
        pass

    return jsonify({
        "message": "upload material"
    })