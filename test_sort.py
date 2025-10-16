from thoughtful_ai import sort

def test_standard():
    assert sort(50, 40, 30, 5) == "STANDARD"

def test_heavy():
    assert sort(50, 40, 30, 25) == "SPECIAL"

def test_bulky():
    assert sort(160, 40, 30, 5) == "SPECIAL"

def test_rejected():
    assert sort(160, 100, 40, 25) == "REJECTED"

def test_type_error():
    try:
        sort(50, 40, "abc", 5)
    except TypeError:
        assert True
    else:
        assert False

def test_value_error():
    try:
        sort(-50, 40, 30, 5)
    except ValueError:
        assert True
    else:
        assert False

if __name__ == "__main__":
    test_standard()
    test_heavy()
    test_bulky()
    test_rejected()
    test_type_error()
    test_value_error()
    print("All tests passed!")