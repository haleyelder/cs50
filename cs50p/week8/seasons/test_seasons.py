import pytest
from seasons import add_text

def test_seasons():
    assert add_text("525600") == "Five hundred twenty-five thousand, six hundred minutes"