import unittest
from sequences.smallest_difference import *


class TestSmallestDifference(unittest.TestCase):
    def test_when_array_is_empty_then_raise_error(self):
        self.assertRaises(ValueError, smallest_difference, [], [1])
        self.assertRaises(ValueError, smallest_difference, [1], [])

    def test_when_either_array_is_length_one(self):
        self.assertEqual(smallest_difference(
            a=[1],
            b=[1]
        ), 0)
        self.assertEqual(smallest_difference(
            a=[1],
            b=[3, 2]
        ), 1)
        self.assertEqual(smallest_difference(
            a=[3, 2],
            b=[1]
        ), 1)

    def test_when_arrays_are_length_two(self):
        self.assertEqual(smallest_difference(
            a=[10, 20],
            b=[5, 21]
        ), 1)

    def test_given_arrays_of_unequal_length_when_pair_is_last_element(self):
        self.assertEqual(smallest_difference(
            a=[10, 20, 30, 40],
            b=[7, 14, 25, 38, 39]
        ), 1)

    def test_given_example_1(self):
        self.assertEqual(smallest_difference(
            a=[1, 2, 3, 11, 15],
            b=[8, 9, 23, 127, 135]
        ), 2)

    def test_given_example_2(self):
        self.assertEqual(smallest_difference(
            a=[1, 2, 11, 15],
            b=[4, 12, 19, 23, 127, 135]
        ), 1)


if __name__ == '__main__':
    unittest.main()
