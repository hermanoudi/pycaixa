import pytest
from click.testing import CliRunner

from mouracx.cli import load, main

from .constants import EXTRACT_FILE

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """test command load"""
    out = cmd.invoke(load, EXTRACT_FILE)
    assert "Moura Fluxo de Caixa" in out.output


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command(wrong_command):
    """test command load"""
    out = cmd.invoke(main, wrong_command, EXTRACT_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
