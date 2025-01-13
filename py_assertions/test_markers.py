import pytest

@pytest.mark.sanity
@pytest.mark.str
def test_strjoin():
    s1 =  'Python,Pytest and Automation'
    t1 = ['Python,Pytest', 'and', 'Automation']
    t2 = ['Python', 'Pytest and Automation']
    assert ' '.join(t1) == s1
