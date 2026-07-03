import os

from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI

# Load environment variables
load_dotenv()

# Synchronous client (LLM)
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Asynchronous client (TTS)
async_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)