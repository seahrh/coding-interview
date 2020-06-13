from dynamicprogramming.edit_distance import *


class TestEditDistance:
    def test_edit_distance(self):
        assert edit_distance("", "") == 0
        assert edit_distance("a", "") == 1
        assert edit_distance("", "a") == 1
        assert edit_distance("ab", "ab") == 0
        assert edit_distance("ab", "ac") == 1
        assert edit_distance("ac", "ab") == 1
        assert edit_distance("ab", "cd") == 2
        assert edit_distance("cd", "ab") == 2
        assert edit_distance("fast", "cats") == 3
        assert edit_distance("cats", "fast") == 3
        assert edit_distance("sunday", "saturday") == 3
        assert edit_distance("saturday", "sunday") == 3
