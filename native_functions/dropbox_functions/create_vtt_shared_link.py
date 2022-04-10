import json
import requests

def create_vtt_shared_link(access_token, new_folder, path_display, url, headers):
    path_display = "{}/{}.vtt".format(path_display, new_folder)
    print("Path Display", path_display)

    data = {
        "path": path_display
    }

    vtt_shared_link = requests.post(
        url,
        headers = headers,
        data = json.dumps(data)
    )

    vtt_shared_link = vtt_shared_link.content
    vtt_shared_link = json.loads(vtt_shared_link.decode("utf-8"))
    vtt_shared_link = vtt_shared_link["url"]
    vtt_shared_link = vtt_shared_link.replace("?dl=0", "?raw=1")

    return vtt_shared_link