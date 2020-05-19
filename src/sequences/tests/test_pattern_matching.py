import unittest
from sequences.pattern_matching import *


class TestPatternMatching(unittest.TestCase):
    def test_given_empty_pattern_then_raise_error(self):
        self.assertRaises(ValueError, matches, '', 'value')

    def test_given_empty_value_then_return_false(self):
        self.assertEqual(matches(pattern='a', value=''), False)

    def test_given_single_pattern_a_then_return_true(self):
        self.assertEqual(matches(pattern='a', value='value'), True)

    def test_given_single_pattern_b_then_return_true(self):
        self.assertEqual(matches(pattern='b', value='value'), True)

    def test_given_example(self):
        value = 'catcatgocatgo'
        self.assertEqual(matches(pattern='aabab', value=value), True)
        self.assertEqual(matches(pattern='aab', value=value), True)
        self.assertEqual(matches(pattern='abb', value=value), True)
        self.assertEqual(matches(pattern='ab', value=value), True)
        self.assertEqual(matches(pattern='a', value=value), True)
        self.assertEqual(matches(pattern='b', value=value), True)
        self.assertEqual(matches(pattern='aba', value=value), False)
        self.assertEqual(matches(pattern='aaba', value=value), False)


if __name__ == '__main__':
    unittest.main()
