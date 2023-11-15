import unittest

class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print("I will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def test_methodC(self):
        print("Running method C")

    def test_methodD(self):
        print("Running method D")

    def test_methodE(self):
        print("Running method E")

    def tearDown(self):
        print("I will run after every testdemo")

if __name__ == '__main__':
    unittest.main(verbosity=2)
#python -m unittest samplee1.py

