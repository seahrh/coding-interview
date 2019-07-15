import unittest
from trees.trie import *


class TestTrie(unittest.TestCase):
    def test_tree_constructor_then_add_words(self):
        t = Trie(['ab', 'aa'])
        t.add('ac')
        self.assertEqual('aa' in t, True)
        self.assertEqual('ab' in t, True)
        self.assertEqual('ac' in t, True)
        self.assertEqual('ad' in t, False)
        self.assertEqual('d' in t, False)

    def test_remove_given_only_one_word(self):
        t = Trie(['a'])
        self.assertEqual('a' in t, True)
        t.remove('a')
        self.assertEqual('a' in t, False)
        t = Trie(['abc'])
        self.assertEqual('abc' in t, True)
        t.remove('abc')
        self.assertEqual('abc' in t, False)

    def test_remove_given_word_that_does_not_exist_then_do_nothing(self):
        t = Trie(['abc'])
        t.remove('abd')
        self.assertEqual('abc' in t, True)
        self.assertEqual('abd' in t, False)

    def test_tree_constructor_then_remove_everything(self):
        t = Trie(['ab', 'aa', 'ac'])
        self.assertEqual('aa' in t, True)
        self.assertEqual('ab' in t, True)
        self.assertEqual('ac' in t, True)
        self.assertEqual('zz' in t, False)
        t.remove('ab')
        t.remove('aa')
        t.remove('ac')
        self.assertEqual('aa' in t, False)
        self.assertEqual('ab' in t, False)
        self.assertEqual('ac' in t, False)
        self.assertEqual('zz' in t, False)

    def test_given_example_1(self):
        t = Trie(['i', 'is', 'pp', 'ms'])
        self.assertEqual('i' in t, True)
        self.assertEqual('is' in t, True)
        self.assertEqual('pp' in t, True)
        self.assertEqual('ms' in t, True)
        self.assertEqual('p' in t, True)
        self.assertEqual('m' in t, True)
        self.assertEqual('s' in t, False)
        self.assertEqual('z' in t, False)

    def test_prefixes_1(self):
        t = Trie(['i', 'is', 'pp', 'ms'])
        self.assertListEqual(t.prefixes('isppms'), ['i', 'is'])
        self.assertListEqual(t.prefixes('ppmsis'), ['pp'])
        self.assertListEqual(t.prefixes('msppis'), ['ms'])
        self.assertListEqual(t.prefixes('zzis'), [])

    def test_prefixes_2(self):
        t = Trie(['b', 'i', 's', 'a'])
        self.assertListEqual(t.prefixes('bibs'), ['b'])
        self.assertListEqual(t.prefixes('ibs'), ['i'])
        self.assertListEqual(t.prefixes('bs'), ['b'])
        self.assertListEqual(t.prefixes('s'), ['s'])


if __name__ == '__main__':
    unittest.main()
