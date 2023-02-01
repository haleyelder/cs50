from twttr import shorten

def test_shorten():
    assert shorten("testing") == "tstng"
    assert shorten("this is my tweet!") == "ths s my twt!"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("s0meth1ng") == "s0mth1ng"