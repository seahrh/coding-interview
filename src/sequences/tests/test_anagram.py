from sequences.anagram import *


class TestAnagram:
    def test_strings_of_length_one(self):
        assert is_anagram('a', 'a')
        assert not is_anagram('a', 'b')

    def test_strings_of_unequal_lengths(self):
        assert not is_anagram('a', 'ab')

    def test_when_strings_are_anagram_then_return_true(self):
        assert is_anagram('test', 'sett')
        assert is_anagram('listen', 'silent')
        assert is_anagram('anagram', 'nagaram')
        assert is_anagram('dusty', 'study')
        assert is_anagram('night', 'thing')

    def test_when_strings_are_not_anagram_then_return_false(self):
        assert not is_anagram('test', 'sets')
