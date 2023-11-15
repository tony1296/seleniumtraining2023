import pytest

def test_demo1_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo1 method A")

def test_demo2_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")

#py.test -v -s test_conftest_demo1.py