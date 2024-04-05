import pytest
from session import add_numbers


def test_add_positive():
    assert add_numbers(1, 2) == 3


def test_add_negative():
    assert add_numbers(-1, -2) == -3


def test_add_type_error():
    with pytest.raises(TypeError):
        add_numbers(4, "world")
