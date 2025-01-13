import sys
import pytest

pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason="Works only on windows")

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

print ("This is the sys version info" + str(sys.version_info))
print (cent_to_fah())

#@pytest.mark.skip("Skipping for no reason specified")
#@pytest.mark.skipif(cent_to_fah()==32, reason="default value test, so skipping")
def test_case01():
    assert type(const) == float

#@pytest.mark.skipif(sys.version_info > (3,11), reason="Does not work on version py above 3,11")
def test_case02():
    assert cent_to_fah() == 32

@pytest.mark.skipif(pytest.__version__ < '5.5.0', reason='pytest version is less, version is ' + str(pytest.__version__))
def test_case03():
    assert cent_to_fah(38) == 100.4

