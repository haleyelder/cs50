from um import count

def test_count():
    assert count("um") == 1
    assert count('album') == 0
    assert count("Um, thanks, um...") == 2