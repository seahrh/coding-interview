from branchbound.zero_one_knapsack import *


class TestZeroOneKnapsackBB:
    def test_two_items_or_less(self):
        assert knapsack(capacity=0, weights=[2], values=[1]) == {(False,)}
        assert knapsack(capacity=1, weights=[2], values=[1]) == {(False,)}
        assert knapsack(capacity=1, weights=[0.1], values=[1]) == {(True,)}
        assert knapsack(capacity=1, weights=[0.1, 2], values=[1, 10]) == {(True, False)}
        assert knapsack(capacity=1, weights=[1, 1], values=[1, 10]) == {(False, True)}
        assert knapsack(capacity=2, weights=[1, 1.9], values=[1, 10]) == {(False, True)}
        assert knapsack(capacity=4, weights=[1.1, 2.2], values=[1, 10]) == {
            (True, True)
        }
        assert knapsack(capacity=1, weights=[0.9, 0.9], values=[1, 1]) == {
            (True, False),
            (False, True),
        }

    def test_case_1(self):
        assert knapsack(capacity=8, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (
                False,
                True,
                True,
                False,
            )
        }
        assert knapsack(capacity=9, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (
                True,
                False,
                True,
                False,
            )
        }
        assert knapsack(capacity=10, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (
                True,
                False,
                True,
                False,
            )
        }
        assert knapsack(capacity=11, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (
                True,
                False,
                True,
                True,
            )
        }
        assert knapsack(capacity=12, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (
                True,
                True,
                True,
                False,
            )
        }
        assert knapsack(capacity=15, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (
                True,
                True,
                True,
                True,
            )
        }
        assert knapsack(capacity=7, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (True, True, False, False),
            (False, False, True, True),
        }
        assert knapsack(capacity=6, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (False, False, True, False),
            (True, False, False, True),
        }
        assert knapsack(capacity=5, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (False, False, True, False)
        }
        assert knapsack(capacity=4, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (True, False, False, False)
        }
        assert knapsack(capacity=3, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (False, True, False, False)
        }
        assert knapsack(capacity=2, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (False, False, False, True)
        }
        assert knapsack(capacity=1, weights=[4, 3, 5, 2], values=[5, 2, 6, 1]) == {
            (False, False, False, False)
        }

    def test_case_2(self):
        assert knapsack(capacity=5, weights=[3, 1, 2], values=[12, 6, 10]) == {
            (
                True,
                False,
                True,
            )
        }
        assert knapsack(capacity=7, weights=[3, 1, 2], values=[12, 6, 10]) == {
            (
                True,
                True,
                True,
            )
        }
        assert knapsack(capacity=4, weights=[3, 1, 2], values=[12, 6, 10]) == {
            (
                True,
                True,
                False,
            )
        }
        assert knapsack(capacity=3, weights=[3, 1, 2], values=[12, 6, 10]) == {
            (
                False,
                True,
                True,
            )
        }
        assert knapsack(capacity=2, weights=[3, 1, 2], values=[12, 6, 10]) == {
            (
                False,
                False,
                True,
            )
        }
        assert knapsack(capacity=1, weights=[3, 1, 2], values=[12, 6, 10]) == {
            (
                False,
                True,
                False,
            )
        }

    def test_case_3(self):
        assert knapsack(capacity=15, weights=[6, 2, 4, 9], values=[12, 10, 10, 18]) == {
            (False, True, True, True)
        }
