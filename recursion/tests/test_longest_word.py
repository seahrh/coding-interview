import unittest
from recursion.longest_word import *


class TestLongestWord(unittest.TestCase):
    def test_given_empty_array_then_return_none(self):
        self.assertEqual(longest_word([]), None)

    def test_given_example_1(self):
        self.assertEqual(longest_word(['ab', 'a', 'b', 'abba']), 'abba')

    def test_given_example_2(self):
        self.assertEqual(longest_word(
            ['spellingbeetest', 'test', 'spelling', 'bee']), 'spellingbeetest')


if __name__ == '__main__':
    unittest.main()
