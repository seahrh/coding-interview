from dynamicprogramming.subset_sum import *


class TestSubsetSumDP:
    def test_when_nothing_can_fit_then_return_empty_set(self):
        assert subset_sum(capacity=1, weights=set()) == set()

    def test_two_items_or_less(self):
        assert subset_sum(capacity=1, weights={1}) == {1}
        assert subset_sum(capacity=1, weights={2}) == set()
        assert subset_sum(capacity=2, weights={1}) == set()
        assert subset_sum(capacity=4, weights={1, 2}) == set()
        assert subset_sum(capacity=3, weights={1, 2}) == {1, 2}
        assert subset_sum(capacity=2, weights={1, 2}) == {2}
        assert subset_sum(capacity=1, weights={1, 2}) == {1}

    def test_case_1(self):
        a = subset_sum(capacity=30, weights={5, 10, 12, 13, 15, 18})
        assert a == {18, 12} or a == {10, 5, 15} or a == {13, 12, 5}
        a = subset_sum(capacity=28, weights={5, 10, 12, 13, 15, 18})
        assert a == {10, 13, 5} or a == {10, 18} or a == {13, 15}
        assert subset_sum(capacity=29, weights={5, 10, 12, 13, 15, 18}) == set()

    def test_case_2(self):
        a = subset_sum(capacity=9, weights={3, 34, 4, 12, 5, 2})
        assert a == {4, 5} or a == {2, 3, 4}
        assert subset_sum(capacity=30, weights={3, 34, 4, 12, 5, 2}) == set()
