import unittest
from trees.trie import *


class TestTrie(unittest.TestCase):
    def test_given_words_of_length_two_only(self):
        t = Trie(['ab', 'aa'])
        self.assertEqual('ab' in t, True)
        self.assertEqual('aa' in t, True)
        self.assertEqual('ac' in t, False)
        self.assertEqual('a' in t, True)
        self.assertEqual('b' in t, False)


if __name__ == '__main__':
    unittest.main()
