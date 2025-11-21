import src.adict as a

def test_add():
    test = a.add({"a":1},{"a":2})
    assert test["a"] == 3