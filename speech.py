import asyncio
import speech_recognition as sr

from openai.helpers import LocalAudioPlayer

from config import async_client


async def tts(speech: str):
    """
    Convert text into speech and play it.
    """

    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Always speak in a cheerful and friendly manner.",
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)


def create_recognizer():
    """
    Create and configure the speech recognizer.
    """

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 2

    return recognizer


def setup_microphone(recognizer):
    """
    Configure the microphone for ambient noise.
    """

    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    return microphone


def speech_to_text(recognizer, microphone):
    """
    Listen from microphone and convert speech to text.
    """

    with microphone as source:

        print("🎤 Please speak something...")

        audio = recognizer.listen(source)

    print("🔄 Converting speech to text...")

    return recognizer.recognize_google(audio)


def speak(text: str):
    """
    Helper function to play TTS.
    """

    asyncio.run(tts(text))