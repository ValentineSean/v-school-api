import os
import dropbox

from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("DROPBOX_ACCESS_TOKEN")
dropbox_path = "/v-school/test/the dev.mp3"
local_path = "././media_files/What are Sets.mp3"

def upload_files():
    dropbox_client = dropbox.Dropbox(access_token)

    file_to_upload = open(local_path, "rb").read()

    dropbox_client.files_upload(f=file_to_upload, path=dropbox_path, autorename=True)

    print("Done uploading :)")