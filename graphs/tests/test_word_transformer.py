import unittest
from graphs.word_transformer import *


class TestWordTransformer(unittest.TestCase):
    def test_given_empty_dictionary_then_return_empty_deque(self):
        self.assertListEqual(list(transform(
            from_word='damp', to_word='like', words=set())), [])

    def test_given_words_of_unequal_length_then_raise_error(self):
        self.assertRaises(ValueError, transform, 'dam', 'like',
                          {'lamp', 'limp', 'lime', 'like'})

    def test_given_only_one_transformation_required(self):
        self.assertListEqual(list(transform(
            from_word='damp', to_word='lamp', words={'lamp', 'damp', 'lime', 'like'})),
            ['damp', 'lamp'])

    def test_given_path_exists_then_return_list_of_transformations(self):
        self.assertListEqual(list(transform(
            from_word='damp', to_word='like',
            words={'damp', 'lamp', 'limp', 'lime', 'like'})),
            ['damp', 'lamp', 'limp', 'lime', 'like'])

    def test_given_path_does_not_exists_then_return_empty_deque(self):
        self.assertListEqual(list(transform(
            from_word='damp', to_word='like',
            words={'damp', 'lamp', 'limp', 'lake', 'like'})),
            [])


if __name__ == '__main__':
    unittest.main()
