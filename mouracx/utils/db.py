from sqlmodel import Session, select, create_engine
from mouracx.models import Movement
from mouracx.settings import SQL_CON_STRING

engine = create_engine(SQL_CON_STRING, echo=False)

def add_movement(session: Session, instance: Movement):
    """Saves movement data to database"""
    session.add(instance)
    return instance

def list_all_movements():
    with Session(engine) as session:
        sql = select(Movement)
        movements = session.exec(sql).all()
    return movements
