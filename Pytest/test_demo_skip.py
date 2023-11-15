import sys
import pytest

@pytest.mark.skip
def test_windows_1():
    print("windows1")

@pytest.mark.skip(reason="Not included inthis build")
def test_windows_2():
    print("windows2")

@pytest.mark.skipif(sys.version_info< (3,6), reason="requires python latest version")
def test_mac_1():
    print("mac1")
#To execute all the tests below one is the command
#py.test test_demo_skip.py -v -rxs
@pytest.mark.mac
def test_mac_2():
    print("mac2")
#py.test.mark.skip
#py.test.mark.skip(reason="")
#py.test -v -rxs
#py.test test_demo_skip.py -m mac -v