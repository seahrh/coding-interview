import unittest
from sequences.peano_numbers import *


class TestPeanoNumbers(unittest.TestCase):
    def test_to_int(self):
        self.assertEqual(to_int(None), 0)
        self.assertEqual(to_int(Num(None)), 1)
        self.assertEqual(to_int(Num(Num(None))), 2)
        self.assertEqual(to_int(Num(Num(Num(None)))), 3)

    def test_from_int(self):
        self.assertEqual(from_int(0), None)
        self.assertEqual(from_int(1), Num(None))
        self.assertEqual(from_int(2), Num(Num(None)))
        self.assertEqual(from_int(3), Num(Num(Num(None))))


if __name__ == '__main__':
    unittest.main()
