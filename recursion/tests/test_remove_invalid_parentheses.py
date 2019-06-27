import unittest
from recursion.remove_invalid_parentheses import *


class TestRemoveInvalidParentheses(unittest.TestCase):
    @unittest.skip
    def test_given_empty_string_then_return_empty_list(self):
        self.assertListEqual(remove(''), [''])

    @unittest.skip
    def test_given_string_starts_with_closing_bracket_then_return_empty_list(self):
        self.assertListEqual(remove(')('), [''])




if __name__ == '__main__':
    unittest.main()
