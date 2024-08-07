import pytest
from subprocess import check_output

@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """test command load"""
    out = check_output(["mouracx", "load", "integration/assets/extrato.csv"]).decode("UTF-8").split("\n")
    assert len(out) > 0

