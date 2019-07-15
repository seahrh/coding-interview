import unittest
from trees.multisearch import *


class TestMultiSearchWithBigStringTrie(unittest.TestCase):
    def test_given_small_strings_of_length_one(self):
        self.assertDictEqual(multisearch_with_bstrie('bibs', ['b', 'i', 's', 'a']),
                             {'b': [0, 2], 'i': [1], 's': [3], 'a': []})

    def test_given_example_1(self):
        self.assertDictEqual(multisearch_with_bstrie('mississippi',
                                                     ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']),
                             {'hi': [],
                              'i': [1, 4, 7, 10],
                              'is': [1, 4],
                              'ppi': [8],
                              'sis': [3],
                              'ssippi': [5]})


if __name__ == '__main__':
    unittest.main()
