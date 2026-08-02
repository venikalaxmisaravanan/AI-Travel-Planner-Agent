import json
from pathlib import Path

# -------------------------------
# File Paths
# -------------------------------

TRIPS_FILE = Path("data/saved_trips.json")
PREFERENCES_FILE = Path("data/user_preferences.json")
DESTINATIONS_FOLDER = Path("data/destinations")


# -------------------------------
# Helper Functions
# -------------------------------

def load_json(file_path, default):
    """
    Load JSON data from a file.
    If the file doesn't exist, return the given default value.
    """
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(file_path, data):
    """
    Save Python data as JSON.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ==========================================================
# TOOL 1 : Save Trip Plan
# ==========================================================

def save_trip_plan(destination, duration, budget, notes=""):

    trips = load_json(TRIPS_FILE, [])

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
                "description": "The travel destination."
            },
            "duration": {
                "type": "string",
                "description": "Trip duration."
            },
            "budget": {
                "type": "string",
                "description": "Budget / Mid-range / Luxury."
            },
            "notes": {
                "type": "string",
                "description": "Additional notes."
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


# ==========================================================
# TOOL 2 : Save User Preferences
# ==========================================================

def save_user_preference(
    budget,
    traveler_type,
    travel_style,
    food_preference="Not specified"
):

    preferences = load_json(PREFERENCES_FILE, {})

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
    "description": "Save the user's travel preferences.",
    "parameters": {
        "type": "object",
        "properties": {
            "budget": {
                "type": "string"
            },
            "traveler_type": {
                "type": "string"
            },
            "travel_style": {
                "type": "string"
            },
            "food_preference": {
                "type": "string"
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


# ==========================================================
# TOOL 3 : Recommend Destination
# ==========================================================

def recommend_destination():

    destination_information = []

    for file in sorted(DESTINATIONS_FOLDER.glob("*.txt")):
        with open(file, "r", encoding="utf-8") as f:
            destination_information.append(f.read())

    return "\n\n".join(destination_information)


recommend_destination_json = {
    "name": "recommend_destination",
    "description": "Retrieve travel information for all supported destinations.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False
    }
}


# ==========================================================
# TOOL 4 : Get Saved Trip
# ==========================================================

def get_saved_trip(destination):

    trips = load_json(TRIPS_FILE, [])

    for trip in trips:
        if trip["destination"].lower() == destination.lower():
            return trip

    return {
        "status": "not_found",
        "message": f"No saved trip found for {destination}."
    }


get_saved_trip_json = {
    "name": "get_saved_trip",
    "description": "Retrieve a previously saved trip.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "Destination name."
            }
        },
        "required": [
            "destination"
        ],
        "additionalProperties": False
    }
}


# ==========================================================
# Register Tools
# ==========================================================

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


# ==========================================================
# Execute Tool Calls
# ==========================================================

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