import unittest
from Pyunit.seleniumdemo import MyTestCase
from Pyunit.samplee1 import TestCaseDemo1
from Pyunit.assertdemo import AssertDemo
from Pyunit.seleniumdemo1 import MyTestCase1

#get all tests from TestClass1 and TestClass2

tc1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)
tc4 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase1)

#Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
#https://docs.python.org/3/library/unittest.html