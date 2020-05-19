from trees.trie import *


class TestTrie:
    def test_tree_constructor_then_add_words(self):
        t = Trie(['ab', 'aa'])
        t.add('ac')
        assert 'aa' in t
        assert 'ab' in t
        assert 'ac' in t
        assert 'ad' not in t
        assert 'd' not in t

    def test_remove_given_only_one_word(self):
        t = Trie(['a'])
        assert 'a' in t
        t.remove('a')
        assert 'a' not in t
        t = Trie(['abc'])
        assert 'abc' in t
        t.remove('abc')
        assert 'abc' not in t

    def test_remove_given_word_that_does_not_exist_then_do_nothing(self):
        t = Trie(['abc'])
        t.remove('abd')
        assert 'abc' in t
        assert 'abd' not in t

    def test_tree_constructor_then_remove_everything(self):
        t = Trie(['ab', 'aa', 'ac'])
        assert 'aa' in t
        assert 'ab' in t
        assert 'ac' in t
        assert 'zz' not in t
        t.remove('ab')
        t.remove('aa')
        t.remove('ac')
        assert 'aa' not in t
        assert 'ab' not in t
        assert 'ac' not in t
        assert 'zz' not in t

    def test_given_example_1(self):
        t = Trie(['i', 'is', 'pp', 'ms'])
        assert 'i' in t
        assert 'is' in t
        assert 'pp' in t
        assert 'ms' in t
        assert 'p' in t
        assert 'm' in t
        assert 's' not in t
        assert 'z' not in t

    def test_prefixes_1(self):
        t = Trie(['i', 'is', 'pp', 'ms'])
        assert t.prefixes('isppms') == ['i', 'is']
        assert t.prefixes('ppmsis') == ['pp']
        assert t.prefixes('msppis') == ['ms']
        assert t.prefixes('zzis') == []

    def test_prefixes_2(self):
        t = Trie(['b', 'i', 's', 'a'])
        assert t.prefixes('bibs') == ['b']
        assert t.prefixes('ibs') == ['i']
        assert t.prefixes('bs') == ['b']
        assert t.prefixes('s') == ['s']
