import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("i will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("i will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def test_methodC(self):
        print("Running method C")    

    def tearDown(self):
        print("I will run after every testdemo")

if __name__ == '__main__':
    unittest.main(verbosity=2)