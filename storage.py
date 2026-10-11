
"""JSON storage for CampusFlow tickets."""

import json
from pathlib import Path


DEFAULT_STORAGE_PATH = Path("data/tickets.json")


def load_tickets(path=DEFAULT_STORAGE_PATH):
    """Load tickets from a JSON file.

    Return an empty list if the file does not exist.
    Raise ValueError if the JSON is malformed or has an invalid structure.
    """
    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Cannot load tickets: {file_path} contains invalid JSON."
        ) from error

    if not isinstance(tickets, list):
        raise ValueError(
            f"Cannot load tickets: {file_path} must contain a JSON list."
        )

    if not all(isinstance(ticket, dict) for ticket in tickets):
        raise ValueError(
            f"Cannot load tickets: every item in {file_path} must be an object."
        )

    return tickets


def save_tickets(tickets, path=DEFAULT_STORAGE_PATH):
    """Save a list of ticket dictionaries to a JSON file."""
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be provided as a list.")

    if not all(isinstance(ticket, dict) for ticket in tickets):
        raise ValueError("Every ticket must be a dictionary.")

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4, ensure_ascii=False)
        file.write("\n")
