import os
import pytest
import uuid
from mouracx.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print("roda antes dos testes desse modulo\n")

def teardown_module():
    print("roda após os testes desse modulo\n")



@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira..")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test Load Funcition"""

    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))

    with open(filepath, "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) > 0
    assert load(PEOPLE_FILE)[0][0] == '3'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test Load Funcition"""
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) > 0
    assert load(PEOPLE_FILE)[0][0] == '3'
