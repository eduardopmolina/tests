import pytest

@pytest.mark.xfail(reason="known issue")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[10]

@pytest.mark.xfail(reason="known issue2")
def test_str05():
    letters2 = ('abcdef')
    assert letters2[5]