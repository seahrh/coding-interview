from permutations.pair_sum import *


class TestPairSum:
    def test_given_empty_array_then_return_empty_set(self):
        assert pair_sum(arr=[], summ=1) == set()

    def test_when_array_length_is_one_then_return_empty_set(self):
        assert pair_sum(arr=[1], summ=1) == set()

    def test_single_pair_found(self):
        assert pair_sum(arr=[1, 2], summ=3) == {(1, 2)}
        assert pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=4) == {(1, 3)}
        assert pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-5) == {(-3, -2)}

    def test_many_pairs_found(self):
        assert pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=2) == {(0, 2), (-1, 3)}
        assert pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-1) == {
            (-3, 2),
            (-2, 1),
            (-1, 0),
        }


class TestPairSumSorted:
    def test_given_empty_array_then_return_empty_set(self):
        assert pair_sum_sorted(arr=[], summ=1) == set()

    def test_when_array_length_is_one_then_return_empty_set(self):
        assert pair_sum_sorted(arr=[1], summ=1) == set()

    def test_single_pair_found(self):
        assert pair_sum_sorted(arr=[1, 2], summ=3) == {(1, 2)}
        assert pair_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], summ=4) == {(1, 3)}
        assert pair_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], summ=-5) == {(-3, -2)}

    def test_many_pairs_found(self):
        assert pair_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], summ=2) == {
            (0, 2),
            (-1, 3),
        }
        assert pair_sum_sorted(arr=[-3, -2, -1, 0, 1, 2, 3], summ=-1) == {
            (-3, 2),
            (-2, 1),
            (-1, 0),
        }


class TestHasPairSum:
    def test_when_array_length_is_one_then_not_found(self):
        assert not has_pair_sum(arr=[1], summ=1)

    def test_single_pair_found(self):
        assert has_pair_sum(arr=[1, 2], summ=3)
        assert has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=4)
        assert has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-5)

    def test_many_pairs_found(self):
        assert has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=2)
        assert has_pair_sum(arr=[2, -1, 3, -2, 1, -3, 0], summ=-1)

    def test_when_duplicates_equal_sum_then_found(self):
        assert has_pair_sum(arr=[1, 2, 4, 4], summ=8)
        assert has_pair_sum(arr=[4, 1, 2, 4], summ=8)

    def test_when_duplicates_exist_and_pair_do_not_exist_then_not_found(self):
        assert not has_pair_sum(arr=[1, 2, 4, 4], summ=7)
        assert not has_pair_sum(arr=[4, 1, 2, 4], summ=7)
