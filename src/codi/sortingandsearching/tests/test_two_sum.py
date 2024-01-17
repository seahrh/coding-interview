from codi.sortingandsearching.lc0_two_sum import *


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
