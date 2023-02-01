from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("cat") == False
    assert validate("1.230.1000.0") == False
    assert validate("1.300.500.700") == False