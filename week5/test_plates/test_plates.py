from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("PI3.14") == False
    assert is_valid("thisistoolong") == False
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False
    assert is_valid("57EED") == False
    assert is_valid("32") == False