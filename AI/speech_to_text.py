import assemblyai as aai
from dotenv import load_dotenv
import os

load_dotenv()

# SET FILE PATH
# file_path = "New Recording.m4a"
file_path="IMG_2680 2.MOV"


def speech_to_text(file_path):
    aai.settings.api_key = os.getenv("SPEECH_TO_TEXT_KEY")
    config = aai.TranscriptionConfig(auto_highlights=True)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path, config=config)
    return transcript.text

# print(speech_to_text(file_path))
# for result in transcript.auto_highlights.results:
#     print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")
