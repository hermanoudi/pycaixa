import pytest
from datetime import datetime
from mouracx.database import (
    EMPTY_DB,
    connect,
    commit,
    add_movement,
)


# @pytest.mark.unit
# def test_database_schema():
#     db = connect()
#     assert db.keys() == EMPTY_DB.keys()


# @pytest.mark.unit
# def test_commit_database():
#     db = connect()
#     data = {
#         "data": datetime.now().isoformat(),
#         "transacao": "HERMANO TESTE COMMIT",
#         "valor": 1000.65,
#         "tipo": "Recebimento",
#     }

#     db = data
#     commit(db)

#     db = connect()
#     assert db["transacao"] == data["transacao"]


# @pytest.mark.unit
# def test_add_moviment_for_the_first_time():
#     data = {
#         "data": datetime.now().isoformat(),
#         "transacao": "HERMANO TESTE",
#         "valor": 15.65,
#         "tipo": "Pagamento",
#     }
#     db = connect()
#     _, created = add_movement(db, data)
#     commit(db)

#     db = connect()
#     assert created is True
#     assert db["transacao"] == "HERMANO TESTE"
