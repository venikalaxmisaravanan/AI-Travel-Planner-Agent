from pathlib import Path


DESTINATION_FOLDER = Path("data/destinations")


def load_travel_knowledge():
    """
    Reads every destination text file
    and combines them into one knowledge base.
    """

    knowledge = ""

    for file in sorted(DESTINATION_FOLDER.glob("*.txt")):
        with open(file, "r", encoding="utf-8") as f:
            knowledge += f.read()
            knowledge += "\n\n"

    return knowledge