import json
import requests

def create_mp3_shared_link(access_token, new_folder, path_display, url, headers):
    path_display = "{}/{}.mp3".format(path_display, new_folder)
    print("Path Display", path_display)

    data = {
        "path": path_display
    }

    mp3_shared_link = requests.post(
        url,
        headers = headers,
        data = json.dumps(data)
    )

    mp3_shared_link = mp3_shared_link.content
    mp3_shared_link = json.loads(mp3_shared_link.decode("utf-8"))
    mp3_shared_link = mp3_shared_link["url"]
    mp3_shared_link = mp3_shared_link.replace("?dl=0", "?raw=1")

    return mp3_shared_link