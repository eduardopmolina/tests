def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0

# This is a failed test
def test_a2():
    assert 9/5 == 1.5, "failed test intentionaly"

def test_a3():
    assert 9//5 == 1 #interger