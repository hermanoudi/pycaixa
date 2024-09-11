import json

from mouracx.settings import DATABASE_PATH

EMPTY_DB = {"data": {}, "transacao": {}, "valor": {}, "tipo": {}}


def connect() -> dict:
    """Connects to the database, returns dict data"""
    try:
        with open(DATABASE_PATH, "r") as database_file:
            return json.loads(database_file.read())
    except (json.JSONDecodeError, FileNotFoundError):
        return EMPTY_DB


def commit(db):
    """Save db back to the database file."""
    if db.keys() != EMPTY_DB.keys():
        raise RuntimeError("Database Schema is invalid.")

    with open(DATABASE_PATH, "w") as database_file:
        database_file.write(json.dumps(db, indent=4))


def add_movement(db, data={}):
    """Saves movement data to database"""
    movement = db

    created = bool(movement)
    movement.update(data)

    return movement, created
