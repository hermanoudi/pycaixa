import os
import pytest
import uuid
from mouracx.core import load
from .constants import EXTRACT_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_extract_filled(request):
    """Test Load Funcition"""
    assert len(load(EXTRACT_FILE)) > 0



