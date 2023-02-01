import pytest
from fuel import convert, gauge

# return int
def test_convert():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("1/4") == 25
    assert convert("4/4") == 100

# return str
def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"