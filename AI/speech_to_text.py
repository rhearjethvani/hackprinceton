import assemblyai as aai

aai.settings.api_key = "9330f89a343a4fafa0b3305c7442b085"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe(
    "New Recording.m4a"
)
print(transcript.text)
