import unittest
from recursion.remove_invalid_parentheses import *


class TestRemoveInvalidParentheses(unittest.TestCase):

    def test_given_empty_string_then_return_empty_list(self):
        self.assertCountEqual(remove(''), [''])

    def test_given_string_starts_with_closing_bracket_then_return_empty_list(self):
        self.assertCountEqual(remove(')('), [''])

    def test_given_at_least_one_left_bracket_and_one_right_bracket_in_excess(self):
        self.assertCountEqual(remove('()())()'), ["()()()", "(())()"])

    def test_given_non_bracket_characters_exist(self):
        self.assertCountEqual(remove('(a)())()'), ["(a())()", "(a)()()"])


if __name__ == '__main__':
    unittest.main()
