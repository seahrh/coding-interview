import unittest
from sequences.longest_balanced_subsequence import *


class TestLongestBalancedSubsequence(unittest.TestCase):

    @staticmethod
    def _is_left(char):
        return char == 'a'

    @staticmethod
    def _is_right(char):
        return char == '1'

    def test_given_unknown_char_then_raise_error(self):
        self.assertRaises(ValueError, longest_balanced_subsequence,
                          ['@', '1'],
                          TestLongestBalancedSubsequence._is_left,
                          TestLongestBalancedSubsequence._is_right)

    def test_given_array_of_length_one_then_return_none(self):
        self.assertEqual(longest_balanced_subsequence(
            arr=['a'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right), None)
        self.assertEqual(longest_balanced_subsequence(
            arr=['1'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right), None)

    def test_given_array_of_length_two(self):
        self.assertEqual(longest_balanced_subsequence(
            arr=['a', '1'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right), ['a', '1'])
        self.assertEqual(longest_balanced_subsequence(
            arr=['1', 'a'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right), ['1', 'a'])
        self.assertEqual(longest_balanced_subsequence(
            arr=['a', 'a'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right), None)
        self.assertEqual(longest_balanced_subsequence(
            arr=['1', '1'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right), None)

    def test_given_example(self):
        self.assertEqual(longest_balanced_subsequence(
            arr=['a', 'a', 'a', 'a', '1', '1', 'a', '1', '1', 'a', 'a', '1', 'a', 'a', '1',
                 'a', 'a', 'a', 'a', 'a'],
            is_left=TestLongestBalancedSubsequence._is_left,
            is_right=TestLongestBalancedSubsequence._is_right),
            ['a', '1', '1', 'a', '1', '1', 'a', 'a', '1', 'a', 'a', '1'])


if __name__ == '__main__':
    unittest.main()
