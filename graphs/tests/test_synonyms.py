import unittest
from graphs.synonyms import *


class TestSynonyms(unittest.TestCase):
    def test_given_example_1(self):
        names = [('John', 15), ('Jon', 12), ('Chris', 13), ('Kris', 4), ('Christopher', 19)]
        synonyms = [('Jon', 'John'), ('John', 'Johnny'), ('Chris', 'Kris'), ('Chris', 'Christopher')]
        self.assertListEqual(merge(names, synonyms), [('John', 27), ('Chris', 36)])


if __name__ == '__main__':
    unittest.main()
