import time
import json
import requests

def create_vtt_shared_link(access_token, new_folder, path_display, url, headers):
    path_display = "{}/{}.vtt".format(path_display, new_folder)
    print("Path Display", path_display)

    data = {
        "path": path_display
    }

    time.sleep(10)

    r = requests.post(
        url,
        headers = headers,
        data = json.dumps(data)
    )

    print("Done uploading :)")
    print("Now Web VTT shared link :)")

    print(r.content)