import unittest
from trees.word_rectangle import *


class TestWordRectangle(unittest.TestCase):
    def test_given_words_of_length_one_only(self):
        self.assertListEqual(largest_word_rectangle(
            ['a']
        ), [['a']])




if __name__ == '__main__':
    unittest.main()
