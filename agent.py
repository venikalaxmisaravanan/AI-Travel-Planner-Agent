import os

from dotenv import load_dotenv
from openai import OpenAI

from context import system_prompt
from tools import tools, handle_tool_calls

# Load environment variables
load_dotenv(override=True)

# Read Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Create OpenAI-compatible Gemini client
client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def chat(message, history):
    """
    Handles one chat conversation with the user.
    """

    # Start conversation with system prompt
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Add previous conversation
    messages.extend(history)

    # Add latest user message
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    # First LLM call
    response = client.chat.completions.create(
        model="models/gemini-flash-latest",
        messages=messages,
        tools=tools
    )

    # Continue until Gemini no longer requests tools
    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        tool_calls = assistant_message.tool_calls

        # Execute Python tools
        tool_results = handle_tool_calls(tool_calls)

        # Add assistant tool request
        messages.append(assistant_message)

        # Add tool outputs
        messages.extend(tool_results)

        # Ask Gemini to continue after seeing tool outputs
        response = client.chat.completions.create(
            model="models/gemini-flash-latest",
            messages=messages,
            tools=tools
        )

    # Return final answer
    return response.choices[0].message.content