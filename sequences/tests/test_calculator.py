import unittest
from sequences.calculator import *


@unittest.skip
class TestCalculator(unittest.TestCase):
    def test_given_example(self):
        self.assertEqual(calculate('2 * 3 + 5 / 6 * 3 + 15'), 23.5)




if __name__ == '__main__':
    unittest.main()
