import unittest
from trees.heaps.running_median import *


class TestRunningMedian(unittest.TestCase):
    def test_when_no_values_added_then_return_zero(self):
        rm = RunningMedian()
        self.assertEqual(rm.median(), 0)

    def test_when_only_one_value_added(self):
        rm = RunningMedian()
        rm.add(1)
        self.assertEqual(rm.median(), 1)

    def test_when_only_two_values_added(self):
        rm = RunningMedian()
        rm.add(1, 2)
        self.assertEqual(rm.median(), 1.5)

    def test_when_duplicate_values_added(self):
        rm = RunningMedian()
        rm.add(2, 2)
        self.assertEqual(rm.median(), 2)

    def test_when_even_number_of_values_added(self):
        rm = RunningMedian()
        rm.add(-4, -3, -2, -1, 1, 2, 3, 4)
        self.assertEqual(rm.median(), 0)

    def test_when_odd_number_of_values_added(self):
        rm = RunningMedian()
        rm.add(-4, -3, -2, -1, 1, 2, 3)
        self.assertEqual(rm.median(), -1)


if __name__ == '__main__':
    unittest.main()
