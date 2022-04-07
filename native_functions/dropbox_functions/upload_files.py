import os
import shutil
import json
import requests
import traceback
import dropbox

from shutil import make_archive
from dotenv import load_dotenv

load_dotenv()

def upload_files(new_folder):
    print("CURRENT WORKING DIRECTORY", os.getcwd())
    access_token = os.getenv("DROPBOX_ACCESS_TOKEN")
    # local_path = "././media_files/{}/What are Sets.mp3".format(new_folder)
    local_path = None

    # make_archive(
    #     "{}".format(new_folder),
    #     "zip",
    #     root_dir="media_files/{}".format(new_folder),
    #     base_dir="{}".format(new_folder),
    # )

    try:
        make_archive(
            "media_files/{}".format(new_folder),
            "zip",
            root_dir="media_files/{}".format(new_folder),
            base_dir=None,
        )

        obsolete_path = "media_files/{}/".format(new_folder)

        local_path = "media_files/{}.zip".format(new_folder)
        
        dropbox_path = "/v-school/test/{}.zip".format(new_folder)

        shutil.rmtree(obsolete_path)

    except:
        traceback.print_exc()

    dropbox_client = dropbox.Dropbox(access_token)

    file_to_upload = open(local_path, "rb").read()

    file_metadata = dropbox_client.files_upload(f=file_to_upload, path=dropbox_path, autorename=True)

    print(file_metadata.path_display)


    # Create Shared Link
    
    url = "https://api.dropboxapi.com/2/sharing/create_shared_link"

    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json"
    }

    data = {
        "path": file_metadata.path_display
    }

    r = requests.post(
        url,
        headers = headers,
        data = json.dumps(data)
    )

    print("Done uploading :)")

    print(r.content)