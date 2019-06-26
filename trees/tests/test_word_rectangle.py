import unittest
from trees.word_rectangle import *


class TestWordRectangle(unittest.TestCase):
    def test_given_words_of_length_one_only(self):
        self.assertListEqual(largest_word_rectangle(
            ['a']
        ), [['a']])

    def test_given_words_of_length_two_only(self):
        self.assertListEqual(largest_word_rectangle(
            ['ab', 'aa']
        ), [['a', 'a'], ['a', 'b']])

    def test_given_words_of_mixed_lengths(self):
        self.assertListEqual(largest_word_rectangle(
            ['ab', 'aa', 'xyz', 'rst']
        ), [['a', 'a'], ['a', 'b']])
        self.assertListEqual(largest_word_rectangle(
            ['ab', 'aa', 'xyz', 'yxz', 'zzx']
        ), [['x', 'y', 'z'], ['y', 'x', 'z'], ['z', 'z', 'x']])


class TestTrie(unittest.TestCase):
    def test_given_words_of_length_two_only(self):
        t = Trie('ab', 'aa')
        self.assertEqual(t.contains('ab'), True)
        self.assertEqual(t.contains('aa'), True)
        self.assertEqual(t.contains('ac'), False)
        self.assertEqual(t.contains('a'), True)
        self.assertEqual(t.contains('b'), False)


if __name__ == '__main__':
    unittest.main()
