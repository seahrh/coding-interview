import unittest
from graphs.synonyms import *


class TestSynonyms(unittest.TestCase):
    def test_given_empty_names_and_synonyms_then_return_empty_list(self):
        names = []
        synonyms = []
        self.assertListEqual(merge(names, synonyms), [])

    def test_given_empty_synonyms(self):
        names = [('John', 15)]
        synonyms = []
        self.assertListEqual(merge(names, synonyms), [('John', 15)])

    def test_given_all_names_belong_to_same_synonym_group(self):
        names = [('John', 15), ('Jon', 1)]
        synonyms = [('Jon', 'John')]
        self.assertListEqual(merge(names, synonyms), [('John', 16)])

    def test_given_example(self):
        names = [('John', 15), ('Jon', 12), ('Chris', 13), ('Kris', 4), ('Christopher', 19)]
        synonyms = [('Jon', 'John'), ('John', 'Johnny'), ('Chris', 'Kris'), ('Chris', 'Christopher')]
        self.assertListEqual(merge(names, synonyms), [('John', 27), ('Chris', 36)])

    def test_given_synonym_group_of_size_4(self):
        names = [('John', 10),
                 ('Jon', 3),
                 ('Davis', 2),
                 ('Kari', 3),
                 ('Johnny', 11),
                 ('Carlton', 8),
                 ('Carleton', 2),
                 ('Jonathan', 9),
                 ('Carrie', 5)]
        synonyms = [('Jonathan', 'John'),
                    ('Jon', 'Johnny'),
                    ('Johnny', 'John'),
                    ('Kari', 'Carrie'),
                    ('Carleton', 'Carlton')]
        self.assertListEqual(merge(names, synonyms), [
            ('John', 33),
            ('Davis', 2),
            ('Kari', 8),
            ('Carlton', 10)])


if __name__ == '__main__':
    unittest.main()
