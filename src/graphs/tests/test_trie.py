from graphs.trie import *


class TestTrie:
    def test_tree_constructor_then_add_words(self):
        t = Trie(["ab", "aa"])
        t.add("ac")
        assert "aa" in t
        assert "ab" in t
        assert "ac" in t
        assert "ad" not in t
        assert "d" not in t

    def test_remove_given_only_one_word(self):
        t = Trie(["a"])
        assert "a" in t
        t.remove("a")
        assert "a" not in t
        t = Trie(["abc"])
        assert "abc" in t
        t.remove("abc")
        assert "abc" not in t

    def test_remove_given_word_that_does_not_exist_then_do_nothing(self):
        t = Trie(["abc"])
        t.remove("abd")
        assert "abc" in t
        assert "abd" not in t

    def test_tree_constructor_then_remove_everything(self):
        t = Trie(["ab", "aa", "ac"])
        assert "aa" in t
        assert "ab" in t
        assert "ac" in t
        assert "zz" not in t
        t.remove("ab")
        t.remove("aa")
        t.remove("ac")
        assert "aa" not in t
        assert "ab" not in t
        assert "ac" not in t
        assert "zz" not in t


class TestTrieWords:
    def test_words(self):
        t = Trie(["bane", "bag", "boa", "babe", "ball", "band", "boat", "ban"])
        assert t.words("bo") == {"boa", "boat"}
        assert t.words("ban") == {"bane", "band", "ban"}
        assert t.words("bag") == {"bag"}
        assert len(t.words("z")) == 0


class TestTrieFind:
    def test_find(self):
        t = Trie(["e"])
        assert t.find("z") == set()
        assert t.find("e") == {0}
        t = Trie(["babe", "abe", "be", "e"])
        assert t.find("z") == set()
        assert t.find("e") == {3}
        assert t.find("b") == {0, 2}
        assert t.find("be") == {2}
        assert t.find("ab") == {1}
        assert t.find("abe") == {1}
        assert t.find("babe") == {0}
        word = "mississippi"
        suffixes = [word[i:] for i in range(len(word))]
        t = Trie(suffixes)
        assert t.find("z") == set()
        assert t.find("i") == {1, 4, 7, 10}
        assert t.find("ip") == {7}
        assert t.find("iss") == {1, 4}
        assert t.find("miss") == {0}
        assert t.find("si") == {3, 6}
