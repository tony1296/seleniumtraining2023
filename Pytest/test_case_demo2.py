"""
file name should start with test
test method name should start with test

py.test test_mod.py # run tests in module
py.test somepath # run  all tests below some path
py.test test_module.py::test_method # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest

@pytest.fixture()

def setUp():
    print("Running demo2 setup")
    yield
    print("Running demo2 teardown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")