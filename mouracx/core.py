"""Core module of mouracx"""

from mouracx.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load('assets/extrato.csv'))
    2
    """
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
