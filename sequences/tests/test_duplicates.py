import unittest
from sequences.duplicates import *


class TestDuplicates(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(remove_duplicates(''), '')

    def test_strings_of_length_one(self):
        self.assertEqual(remove_duplicates('a'), 'a')

    def test_when_no_duplicates_exist_then_return_original_string(self):
        self.assertEqual(remove_duplicates('abc'), 'abc')

    def test_when_duplicates_exist_then_return_string_without_duplicates(self):
        self.assertEqual(remove_duplicates('aabc'), 'abc')
        self.assertEqual(remove_duplicates('abca'), 'abc')
        self.assertEqual(remove_duplicates('abac'), 'abc')


if __name__ == '__main__':
    unittest.main()
