import os
import dropbox

from shutil import make_archive
from dotenv import load_dotenv

load_dotenv()

def upload_files(new_folder):
    print("CURRENT WORKING DIRECTORY", os.getcwd())
    access_token = os.getenv("DROPBOX_ACCESS_TOKEN")
    dropbox_path = "/v-school/test/what_are_math_sets.mp3"
    local_path = "././media_files/{}/What are Sets.mp3".format(new_folder)

    # make_archive(
    #     "{}".format(new_folder),
    #     "zip",
    #     root_dir="media_files/{}".format(new_folder),
    #     base_dir="{}".format(new_folder),
    # )

    make_archive(
        "media_files/{}".format(new_folder),
        "zip",
        root_dir="media_files/{}".format(new_folder),
        base_dir=None,
    )

    dropbox_client = dropbox.Dropbox(access_token)

    file_to_upload = open(local_path, "rb").read()

    dropbox_client.files_upload(f=file_to_upload, path=dropbox_path, autorename=True)

    print("Done uploading :)")