import unittest

class Test(unittest.TestCase):

    def test_number(self):
        a = 12
        excpeted_value = 12

        self.assertEqual(a, excpeted_value)

if __name__ == "__main__":
    unittest.main()