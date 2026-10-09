import json
import os

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "tickets.json")

def save_tickets(tickets, filepath=FILE_PATH):
    """
    F7 — PERSISTENCE: Save tickets list to JSON file.
    Creates directory automatically if missing.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2)

def load_tickets(filepath=FILE_PATH):
    """
    F7 — PERSISTENCE: Load tickets list from JSON file.
    Returns empty list if file missing; raises ValueError on malformed JSON.
    """
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Corrupted storage file: {filepath}") from e
