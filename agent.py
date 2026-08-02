import os

from dotenv import load_dotenv
from openai import OpenAI

from context import system_prompt

load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def chat(message, history):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )
def chat(message, history):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        model="models/gemini-flash-latest",
        messages=messages
    )

    return response.choices[0].message.content