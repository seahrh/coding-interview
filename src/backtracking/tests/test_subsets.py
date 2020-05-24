from backtracking.subsets import *


class TestSubsets:
    def test_subsets(self):
        assert subsets(arr=[1], k=1) == {frozenset([1])}
        assert subsets(arr=[1, 2, 3, 4], k=4) == {frozenset([1, 2, 3, 4])}
        assert subsets(arr=[1, 2, 3, 4], k=1) == {
            frozenset([1]),
            frozenset([2]),
            frozenset([3]),
            frozenset([4]),
        }
        assert subsets(arr=[1, 2, 3, 4], k=2) == {
            frozenset([1, 2]),
            frozenset([1, 3]),
            frozenset([1, 4]),
            frozenset([2, 3]),
            frozenset([2, 4]),
            frozenset([3, 4]),
        }
        assert subsets(arr=[1, 2, 3, 4], k=3) == {
            frozenset([1, 2, 3]),
            frozenset([1, 3, 4]),
            frozenset([1, 4, 2]),
            frozenset([2, 3, 4]),
            frozenset([2, 4, 1]),
        }
