import unittest
from mathlogic.lexrank import *


class TestLexrank(unittest.TestCase):
    def test_given_empty_string_then_raise_error(self):
        self.assertRaises(ValueError, rank, '')

    def test_given_string_of_length_one_then_return_rank_1(self):
        self.assertEqual(rank('z'), 1)

    def test_given_string_of_length_two(self):
        self.assertEqual(rank('ab'), 1)
        self.assertEqual(rank('ba'), 2)

    def test_given_string_of_length_three(self):
        self.assertEqual(rank('abc'), 1)
        self.assertEqual(rank('acb'), 2)
        self.assertEqual(rank('bac'), 3)
        self.assertEqual(rank('bca'), 4)
        self.assertEqual(rank('cab'), 5)
        self.assertEqual(rank('cba'), 6)

    def test_given_string_of_length_six(self):
        self.assertEqual(rank('string'), 598)


if __name__ == '__main__':
    unittest.main()
