"""Core module of mouracx"""

from csv import reader

from mouracx.database import add_movement, commit, connect
from mouracx.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load('assets/extrato.csv'))
    2
    """
    try:
        csv_data = reader(open(filepath))
        
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
    db = connect()
    movements = []
    headers = ["data", "transacao", "valor", "tipo"]
    for line in csv_data:
        movement_data = dict(zip(headers, [item.strip() for item in line]))
        movement, created = add_movement(db, movement_data)
        return_data = movement.copy()
        return_data["created"] = created
        movements.append(return_data)
    
    commit(db)
    return movements
