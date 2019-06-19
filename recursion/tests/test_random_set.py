import unittest
from recursion.random_set import *


class TestRandomSetRecursive(unittest.TestCase):
    def test_given_array_too_small_to_fill_set(self):
        self.assertRaises(ValueError, pick_rec, [1], 2, 0)

    def test_given_array_of_length_one_and_m_equals_one(self):
        self.assertEqual(pick_rec(arr=[0], m=1, index=0), [0])

    def test_given_array_of_length_two_and_m_is_smaller(self):
        chosen = set()
        for _ in range(10):
            chosen.add(*pick_rec(arr=[0, 1], m=1, index=1))
        self.assertEqual(0 in chosen, True)
        self.assertEqual(1 in chosen, True)

    def test_given_array_of_length_10_and_m_is_smaller(self):
        chosen = set()
        for _ in range(20):
            for v in pick_rec(arr=list(range(10)), m=5, index=9):
                chosen.add(v)
        self.assertEqual(0 in chosen, True)
        self.assertEqual(1 in chosen, True)
        self.assertEqual(2 in chosen, True)
        self.assertEqual(3 in chosen, True)
        self.assertEqual(4 in chosen, True)
        self.assertEqual(5 in chosen, True)
        self.assertEqual(6 in chosen, True)
        self.assertEqual(7 in chosen, True)
        self.assertEqual(8 in chosen, True)
        self.assertEqual(9 in chosen, True)


if __name__ == '__main__':
    unittest.main()
