import unittest
from recursion.string_permutations import *


class TestStringPermutationsWithoutDuplicates(unittest.TestCase):
    def test_when_string_is_empty_then_return_array_with_an_empty_string(self):
        self.assertListEqual(permutate_without_duplicates(''), [''])

    def test_when_string_is_length_one(self):
        self.assertListEqual(permutate_without_duplicates('a'), ['a'])

    def test_when_string_is_length_two(self):
        self.assertListEqual(permutate_without_duplicates('ab'), ['ab', 'ba'])

    def test_when_string_is_length_three(self):
        self.assertListEqual(
            permutate_without_duplicates('abc'), ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])

    def test_when_string_is_length_four(self):
        self.assertListEqual(
            permutate_without_duplicates('abcd'),
            ['abcd', 'bacd', 'bcad', 'bcda',
             'acbd', 'cabd', 'cbad', 'cbda',
             'acdb', 'cadb', 'cdab', 'cdba',
             'abdc', 'badc', 'bdac', 'bdca',
             'adbc', 'dabc', 'dbac', 'dbca',
             'adcb', 'dacb', 'dcab', 'dcba'
             ])


if __name__ == '__main__':
    unittest.main()
