import unittest
from sequences.anagram import *


class TestAnagram(unittest.TestCase):
    def test_strings_of_length_one(self):
        self.assertEqual(is_anagram('a', 'a'), True)
        self.assertEqual(is_anagram('a', 'b'), False)

    def test_strings_of_unequal_lengths(self):
        self.assertEqual(is_anagram('a', 'ab'), False)

    def test_when_strings_are_anagram_then_return_true(self):
        self.assertEqual(is_anagram('test', 'sett'), True)
        self.assertEqual(is_anagram('listen', 'silent'), True)
        self.assertEqual(is_anagram('anagram', 'nagaram'), True)
        self.assertEqual(is_anagram('dusty', 'study'), True)
        self.assertEqual(is_anagram('night', 'thing'), True)

    def test_when_strings_are_not_anagram_then_return_false(self):
        self.assertEqual(is_anagram('test', 'sets'), False)


if __name__ == '__main__':
    unittest.main()
