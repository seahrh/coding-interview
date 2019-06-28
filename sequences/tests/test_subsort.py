import unittest
from sequences.subsort import *


class TestSubSort(unittest.TestCase):
    def test_given_empty_array_then_raise_error(self):
        self.assertRaises(ValueError, subsort, [])

    def test_given_array_of_length_one(self):
        self.assertEqual(subsort([1]), None)

    def test_given_array_of_length_two(self):
        self.assertEqual(subsort([1, 2]), None)
        self.assertEqual(subsort([2, 1]), (0, 1))

    def test_given_array_of_length_three(self):
        self.assertEqual(subsort([1, 2, 3]), None)
        self.assertEqual(subsort([3, 2, 1]), (0, 2))
        self.assertEqual(subsort([2, 1, 3]), (0, 1))
        self.assertEqual(subsort([1, 3, 2]), (1, 2))

    def test_given_array_of_length_four(self):
        self.assertEqual(subsort([1, 2, 3, 4]), None)
        self.assertEqual(subsort([4, 3, 2, 1]), (0, 3))
        self.assertEqual(subsort([2, 3, 1, 4]), (0, 2))
        self.assertEqual(subsort([2, 1, 3, 4]), (0, 1))
        self.assertEqual(subsort([1, 3, 2, 4]), (1, 2))
        self.assertEqual(subsort([1, 4, 2, 3]), (1, 3))
        self.assertEqual(subsort([1, 2, 4, 3]), (2, 3))

    def test_given_example_1(self):
        self.assertEqual(subsort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))

    def test_given_example_2(self):
        self.assertEqual(subsort([30, 40, 39, 50]), (1, 2))


if __name__ == '__main__':
    unittest.main()
