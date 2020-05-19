import unittest
from recursion.shuffle import *


class TestShuffleRecursive(unittest.TestCase):
    def test_given_empty_array_then_return_same_array(self):
        self.assertListEqual(shuffle_rec(cards=[], index=0), [])

    def test_given_array_of_length_one_then_return_same_array(self):
        self.assertListEqual(shuffle_rec(cards=[1], index=0), [1])

    def test_given_negative_index_number_then_raise_error(self):
        self.assertRaises(ValueError, shuffle_rec, [1, 2], -1)

    def test_given_array_of_length_two(self):
        permutations = set()
        for _ in range(20):
            permutations.add(tuple(shuffle_rec(cards=[1, 2], index=1)))
        self.assertEqual(len(permutations), 2)
        self.assertSetEqual(permutations, {(1, 2), (2, 1)})

    def test_given_array_of_length_three(self):
        permutations = set()
        for _ in range(40):
            permutations.add(tuple(shuffle_rec(cards=[1, 2, 3], index=2)))
        self.assertEqual(len(permutations), 6)
        self.assertSetEqual(permutations, {
            (1, 2, 3), (3, 2, 1), (1, 3, 2), (2, 3, 1), (3, 1, 2), (2, 1, 3)})


class TestShuffle(unittest.TestCase):
    def test_given_empty_array_then_return_same_array(self):
        self.assertListEqual(shuffle(cards=[]), [])

    def test_given_array_of_length_one_then_return_same_array(self):
        self.assertListEqual(shuffle(cards=[1]), [1])

    def test_given_array_of_length_two(self):
        permutations = set()
        for _ in range(20):
            permutations.add(tuple(shuffle(cards=[1, 2])))
        self.assertEqual(len(permutations), 2)
        self.assertSetEqual(permutations, {(1, 2), (2, 1)})

    def test_given_array_of_length_three(self):
        permutations = set()
        for _ in range(40):
            permutations.add(tuple(shuffle(cards=[1, 2, 3])))
        self.assertEqual(len(permutations), 6)
        self.assertSetEqual(permutations, {
            (1, 2, 3), (3, 2, 1), (1, 3, 2), (2, 3, 1), (3, 1, 2), (2, 1, 3)})


if __name__ == '__main__':
    unittest.main()
