import os

DATEFMT: str = "%d/%m/%Y %H:%M:%S"
DATEFMT_DATE: str = "%d/%m/%Y"

ROOT_PATH: str = os.path.dirname(__file__)
DATABASE_PATH: str = os.path.join(ROOT_PATH, "..", "assets", "database.db")
SQL_CON_STRING = f"sqlite:///{DATABASE_PATH}"
