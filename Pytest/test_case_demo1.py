import pytest

@pytest.fixture()

def setUp():
    print("Running demo1 setUp")

def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")

def test_demo1_methodC(setUp):
    print("Running demo1 method C")

def test_demo1_methodD(setUp):
    print("Running demo1 method D")

def test_demo1_methodE(setUp):
    print("END")