import pytest

def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

def func1():
    raise ValueError("Exception func 1 raised!")

def test_case02():
    with pytest.raises(Exception) as execinfo:
        #assert(1,2,3) == (1,2,4)
        func1()
    print (str(execinfo))
    assert (str(execinfo.value)) == 'Exception func 1 raised!'
