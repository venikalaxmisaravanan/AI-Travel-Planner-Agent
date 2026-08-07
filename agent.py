import os

from dotenv import load_dotenv
from openai import OpenAI

from context import system_prompt
from tools import tools, handle_tool_calls


# ------------------------------------------
# Load Environment Variables
# ------------------------------------------

load_dotenv()


# ------------------------------------------
# Gemini Client
# ------------------------------------------

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# ------------------------------------------
# Chat Function
# ------------------------------------------

def chat(message, history):

    # Start with the system prompt
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # ------------------------------------------
    # Convert Gradio history to OpenAI format
    # ------------------------------------------

    for msg in history:
        messages.append(
            {
                "role": msg["role"],
                "content": msg["content"]
            }
        )

    # Latest user message
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    # ------------------------------------------
    # First LLM Call
    # ------------------------------------------

    response = client.chat.completions.create(
        model="models/gemini-flash-latest",
        messages=messages,
        tools=tools
    )

    # ------------------------------------------
    # Execute Tools if Requested
    # ------------------------------------------

    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        tool_calls = assistant_message.tool_calls

        tool_results = handle_tool_calls(tool_calls)

        messages.append(assistant_message)

        messages.extend(tool_results)

        response = client.chat.completions.create(
            model="models/gemini-flash-latest",
            messages=messages,
            tools=tools
        )

    # ------------------------------------------
    # Final Response
    # ------------------------------------------

    return response.choices[0].message.content