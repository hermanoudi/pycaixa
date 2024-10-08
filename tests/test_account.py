import pytest

from mouracx.core import register_account


@pytest.mark.unit
@pytest.mark.high
def test_save_account_positive(request):
    """Test Save Account"""
    name = "Conta Teste"
    type_account = "Poupança"
    currency = "BRL"

    account = register_account(name, type_account, currency)
    assert account is not None


@pytest.mark.unit
@pytest.mark.high
def test_save_account_negative(request):
    """Test Save Account negativo"""
    name = "CO"
    type_account = "Errada"
    currency = "BRL"
    with pytest.raises(ValueError):
        account = register_account(name, type_account, currency)
        assert account is not None
