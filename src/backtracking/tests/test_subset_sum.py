from backtracking.subset_sum import *


class TestSubsetSum:
    def test_when_nothing_can_fit_then_return_empty_set(self):
        assert subset_sum(capacity=1, weights=set()) == set()

    def test_two_items_or_less(self):
        assert subset_sum(capacity=1, weights={1}) == {frozenset([1])}
        assert subset_sum(capacity=1, weights={2}) == set()
        assert subset_sum(capacity=2, weights={1}) == set()
        assert subset_sum(capacity=4, weights={1, 2}) == set()
        assert subset_sum(capacity=3, weights={1, 2}) == {frozenset([1, 2])}
        assert subset_sum(capacity=2, weights={1, 2}) == {frozenset([2])}
        assert subset_sum(capacity=1, weights={1, 2}) == {frozenset([1])}

    def test_case_1(self):
        assert subset_sum(capacity=30, weights={5, 10, 12, 13, 15, 18}) == {
            frozenset({18, 12}),
            frozenset({10, 5, 15}),
            frozenset({13, 12, 5}),
        }
