from trees.heaps.running_median import *


class TestRunningMedian:
    def test_when_no_values_added_then_return_zero(self):
        rm = RunningMedian()
        assert rm.median() == 0

    def test_when_only_one_value_added(self):
        rm = RunningMedian()
        rm.add(1)
        assert rm.median() == 1

    def test_when_only_two_values_added(self):
        rm = RunningMedian()
        rm.add(1, 2)
        assert rm.median() == 1.5

    def test_when_duplicate_values_added(self):
        rm = RunningMedian()
        rm.add(2, 2)
        assert rm.median() == 2

    def test_when_even_number_of_values_added(self):
        rm = RunningMedian()
        rm.add(-4, -3, -2, -1, 1, 2, 3, 4)
        assert rm.median() == 0

    def test_when_odd_number_of_values_added(self):
        rm = RunningMedian()
        rm.add(-4, -3, -2, -1, 1, 2, 3)
        assert rm.median() == -1
