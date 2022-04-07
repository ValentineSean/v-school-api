# CREATE SUBTITLES

import datetime as dt

def create_subtitles(utterances, new_folder):
    file_header = "WEBVTT"

    # line_number = 3
    # time_range = "00:00:07.000 --> 00:00:13.000"
    # text = "When the power went away."

    # subtitles_file = open("subtitles.vtt", "a")
    subtitles_file = open("././media_files/{}/{}.vtt".format(new_folder, new_folder), "a")

    subtitles_file.write(file_header)

    for index, section in enumerate(utterances):
        line_number = index + 1

        start_time = section["start"]
        start_time = dt.timedelta(seconds=start_time)
        start_time = str(start_time)[:-3]

        end_time = section["end"]
        end_time = dt.timedelta(seconds=end_time)
        end_time = str(end_time)[:-3]
        
        time_range = start_time + " --> " + end_time
        
        text = section["transcript"]

        subtitles_file.write("\n\n" + str(line_number) + "\n" + time_range + "\n" + text)

    subtitles_file.close()

        # subtitles_file = open("subtitles.vtt", "r")

        # subtitles_content = subtitles_file.read()

    # print(subtitles_content)

# --------------------------

# create_subtitles()