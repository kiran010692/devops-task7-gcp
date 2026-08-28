import pytest
from app import calculate_discount


def test_calculate_discount():
    assert calculate_discount(100, 20) == 80.0
    assert calculate_discount(50, 10) == 45.0


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)