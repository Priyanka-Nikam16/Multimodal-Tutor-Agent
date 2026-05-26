from openai import OpenAI
from dotenv import load_dotenv
from langsmith import traceable
import os
import uuid

load_dotenv()

client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TTS_MODEL="gpt-4o-mini-tts"

@traceable(name="Text to Speech Agent")
def generate_audio(text):
    file_name=f"audio/output_{uuid.uuid4()}.mp3"
    response=client.audio.speech.create(
        model=TTS_MODEL,
        voice="alloy",
        input=text
    )
    response.stream_to_file(file_name)
    return file_name
