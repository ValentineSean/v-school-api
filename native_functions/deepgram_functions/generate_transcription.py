from email.mime import audio
import os
import asyncio
import json

from deepgram import Deepgram
from dotenv import load_dotenv

load_dotenv()

deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

async def main(audio_file_name):
    deepgram = Deepgram(deepgram_api_key)

    with open(audio_file_name, "rb") as audio:
        source = {
            "buffer": audio,
            "mimetype": "audio/mp3"
        }

        response = await deepgram.transcription.prerecorded(source, {"punctuate": True}, numerals=True, utterances=True)
        # response = json.dumps(response, indent=4)
        # response = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        utterances = response["results"]["utterances"]

        # create_subtitles(utterances)
        # for x in response:
        #     print(x["transcript"])
        print(response)

def generate_transcription(audio_file):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(audio_file))