import os
import shutil
from threading import local
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

    dropbox_client.files_upload(f=file_to_upload, path=dropbox_path, autorename=True)

    print("Done uploading :)")