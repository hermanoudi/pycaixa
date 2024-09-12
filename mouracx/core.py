"""Core module of mouracx"""
import csv

from datetime import date
from decimal import Decimal
from mouracx.database import get_session
from mouracx.utils.log import get_logger
from mouracx.utils.db import add_movement, list_all_movements
from mouracx.models import Movement
from typing import List

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load('assets/extrato.csv'))
    2
    """
    movements = []
    try:
        with get_session() as session:
            with open(filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    # Convertendo a data do CSV para o formato de data
                    data = date.fromisoformat(row['data'])
                    valor = Decimal(row['valor'])
                    instance = Movement(data=data, transacao=row['transacao'], valor=valor, tipo=row['tipo'])
                    movement = add_movement(session, instance)
                    returndata = movement.dict(exclude={"id"})
                    movements.append(returndata)
                session.commit()
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    return movements


def list_movements() -> List[Movement]:
    movements = []

    for mov in list_all_movements():
        returndata = mov.dict(exclude={"id"})
        movements.append(returndata)
    return movements
