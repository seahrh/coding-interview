from sequences.majority import *


class TestMajority:
    def test_given_empty_array_then_return_none(self):
        assert majority_element([]) is None

    def test_given_array_of_length_one(self):
        assert majority_element([1]) == 1

    def test_given_array_of_length_two(self):
        assert majority_element([1, 1]) == 1
        assert majority_element([1, -1]) is None

    def test_given_example_1(self):
        assert majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5]) == 5

    def test_given_most_frequent_item_is_not_majority_then_return_none(self):
        assert majority_element([3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]) is None

    def test_given_most_frequent_item_is_majority_then_return_item(self):
        assert majority_element([3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7, 7, 7]) == 7
