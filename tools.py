import json
from pathlib import Path
TRIPS_FILE = Path("data/saved_trips.json")
PREFERENCES_FILE = Path("data/user_preferences.json")
def load_json(file_path):
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def save_trip_plan(destination, duration, budget, notes=""):
    trips = load_json(TRIPS_FILE)
    trip_plan = {
        "destination": destination,
        "duration": duration,
        "budget": budget,
        "notes": notes
    }
    trips.append(trip_plan)
    save_json(TRIPS_FILE, trips)
    return {
    "status": "success",
    "message": f"{destination} trip saved successfully."
}
save_trip_plan_json = {
    "name": "save_trip_plan",
    "description": "Save a travel itinerary for the user.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "The travel destination chosen by the user."
            },
            "duration": {
                "type": "string",
                "description": "How many days the user plans to travel."
            },
            "budget": {
                "type": "string",
                "description": "The user's travel budget such as Budget, Mid-range, or Luxury."
            },
            "notes": {
                "type": "string",
                "description": "Any additional travel preferences or notes."
            }
        },
        "required": [
            "destination",
            "duration",
            "budget"
        ],
        "additionalProperties": False
    }
}
def save_user_preference(
    budget,
    traveler_type,
    travel_style,
    food_preference="Not specified"
):
    preferences = load_json(PREFERENCES_FILE)

    preferences["budget"] = budget
    preferences["traveler_type"] = traveler_type
    preferences["travel_style"] = travel_style
    preferences["food_preference"] = food_preference

    save_json(PREFERENCES_FILE, preferences)

    return {
        "status": "success",
        "message": "User preferences saved successfully."
    }
save_user_preference_json = {
    "name": "save_user_preference",
    "description": "Save the user's travel preferences for future recommendations.",
    "parameters": {
        "type": "object",
        "properties": {
            "budget": {
                "type": "string",
                "description": "The user's travel budget such as Budget, Mid-range, or Luxury."
            },
            "traveler_type": {
                "type": "string",
                "description": "Type of traveler such as Solo, Couple, Family, or Friends."
            },
            "travel_style": {
                "type": "string",
                "description": "Preferred travel style such as Adventure, Nature, Historical, Relaxation, or Spiritual."
            },
            "food_preference": {
                "type": "string",
                "description": "The user's preferred food type, if provided."
            }
        },
        "required": [
            "budget",
            "traveler_type",
            "travel_style"
        ],
        "additionalProperties": False
    }
}
from pathlib import Path

DESTINATIONS_FOLDER = Path("data/destinations")


def recommend_destination():
    destination_information = []

    for file in DESTINATIONS_FOLDER.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            destination_information.append(f.read())

    return "\n\n".join(destination_information)
recommend_destination_json = {
    "name": "recommend_destination",
    "description": "Retrieve travel information about all available destinations so the AI can recommend the most suitable place for the user.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False
    }
}
def get_saved_trip(destination):
    trips = load_json(TRIPS_FILE)

    if destination in trips:
        return trips[destination]

    return {
        "status": "not_found",
        "message": "No saved trip found for this destination."
    }
get_saved_trip_json = {
    "name": "get_saved_trip",
    "description": "Retrieve a previously saved travel itinerary for a destination.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "The destination whose saved itinerary should be retrieved."
            }
        },
        "required": [
            "destination"
        ],
        "additionalProperties": False
    }
}
tools = [
    {
        "type": "function",
        "function": save_trip_plan_json
    },
    {
        "type": "function",
        "function": save_user_preference_json
    },
    {
        "type": "function",
        "function": recommend_destination_json
    },
    {
        "type": "function",
        "function": get_saved_trip_json
    }
]
def handle_tool_calls(tool_calls):
    results = []

    for tool_call in tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(tool_call.function.arguments)

        tool = globals().get(tool_name)

        if tool:
            result = tool(**arguments)
        else:
            result = {
                "status": "error",
                "message": f"Tool '{tool_name}' not found."
            }

        results.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            }
        )

    return results