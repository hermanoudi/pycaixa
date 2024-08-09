from subprocess import CalledProcessError, check_output

import pytest


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """test command load"""
    out = (
        check_output(["mouracx", "load", "integration/assets/extrato.csv"])
        .decode("UTF-8")
        .split("\n")
    )
    assert len(out) > 0


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command(wrong_command):
    """test command load"""
    with pytest.raises(CalledProcessError) as error:
        out = (
            check_output(
                ["mouracx", wrong_command, "integration/assets/extrato.csv"]
            )
            .decode("UTF-8")
            .split("\n")
        )
        assert "non-zero" in str(error.getrepr())
