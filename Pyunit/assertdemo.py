import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a,"a is not false")
        b = False
        self.assertFalse(b,"b is not true")

    def test_assertEqual(self):
        a = "Test"
        b = "Tes"
        self.assertEqual(a, b, msg="'a' is equal to 'b'")
        #self.assetNotEqual(a,b,msg="'a' is not equal to 'b'")

if __name__ == '__main__':
    unittest.main(verbosity=2)