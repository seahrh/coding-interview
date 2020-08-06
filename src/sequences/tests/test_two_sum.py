from sequences.two_sum import *


class TestTwoSum:
    def test_given_empty_array_then_return_empty_set(self):
        assert two_sum(arr=[], target=1) == set()

    def test_when_array_length_is_one_then_return_empty_set(self):
        assert two_sum(arr=[1], target=1) == set()

    def test_single_pair_found(self):
        assert two_sum(arr=[1, 2], target=3) == {(1, 2)}
        assert two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=4) == {(1, 3)}
        assert two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=-5) == {(-3, -2)}

    def test_many_pairs_found(self):
        assert two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=2) == {(0, 2), (-1, 3)}
        assert two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=-1) == {
            (-3, 2),
            (-2, 1),
            (-1, 0),
        }


class TestTwoSumSorted:
    def test_given_empty_array_then_return_empty_set(self):
        assert two_sum_sorted(arr=[], target=1) == set()

    def test_when_array_length_is_one_then_return_empty_set(self):
        assert two_sum_sorted(arr=[1], target=1) == set()

    def test_single_pair_found(self):
        assert two_sum_sorted(arr=[1, 2], target=3) == {(1, 2)}
        assert two_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], target=4) == {(1, 3)}
        assert two_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], target=-5) == {(-3, -2)}

    def test_many_pairs_found(self):
        assert two_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], target=2) == {
            (0, 2),
            (-1, 3),
        }
        assert two_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], target=-1) == {
            (-3, 2),
            (-2, 1),
            (-1, 0),
        }


class TestHasTwoSum:
    def test_when_array_length_is_one_then_not_found(self):
        assert not has_two_sum(arr=[1], target=1)

    def test_single_pair_found(self):
        assert has_two_sum(arr=[1, 2], target=3)
        assert has_two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=4)
        assert has_two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=-5)

    def test_many_pairs_found(self):
        assert has_two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=2)
        assert has_two_sum(arr=[2, -1, 3, -2, 1, -3, 0], target=-1)

    def test_when_duplicates_equal_sum_then_found(self):
        assert has_two_sum(arr=[1, 2, 4, 4], target=8)
        assert has_two_sum(arr=[4, 1, 2, 4], target=8)

    def test_when_duplicates_exist_and_pair_do_not_exist_then_not_found(self):
        assert not has_two_sum(arr=[1, 2, 4, 4], target=7)
        assert not has_two_sum(arr=[4, 1, 2, 4], target=7)
