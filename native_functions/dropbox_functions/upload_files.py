import os
import shutil
import time
import traceback
import dropbox

from shutil import make_archive
from dotenv import load_dotenv

# Shared Links Functions
from .create_vtt_shared_link import create_vtt_shared_link
from .create_mp3_shared_link import create_mp3_shared_link

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

    print("***FILE METADATA***")
    print(file_metadata)

    # -------------------------------------

    path_display = file_metadata.path_display
    path_display = path_display[:-4]

    # Create Shared Link
    
    url = "https://api.dropboxapi.com/2/sharing/create_shared_link"
    # url = "https://api.dropboxapi.com/2/sharing/list_shared_links"

    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json"
    }

    time.sleep(10)

    mp3_shared_link = create_mp3_shared_link(access_token, new_folder, path_display, url, headers)
    # mp3_shared_link = json.loads(mp3_shared_link.decode("utf-8"))

    vtt_shared_link = create_vtt_shared_link(access_token, new_folder, path_display, url, headers)
    # vtt_shared_link = json.loads(vtt_shared_link.decode("utf-8"))

    print("Done uploading :)")

    print("Shared Links:")

    print("MP3 SHARED LINK", mp3_shared_link)
    print("VTT SHARED LINK", vtt_shared_link)