import pytest

@pytest.mark.windows
def test_windows_1():
    print("windows")
@pytest.mark.windows
def test_windows_2():
    print("windows")
@pytest.mark.mac
def test_mac_1():
    print("mac")
@pytest.mark.mac
def test_mac_2():
    print("mac")

#py.test test_demo_skipsample.py -m mac -v
#py.test test_demo_skipsample.py -m windows -v