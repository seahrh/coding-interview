import unittest
from geometry.line_intersection import *


class TestLineIntersection(unittest.TestCase):
    def test_when_lines_are_same_segments_then_return_intersection_point_with_smallest_x(self):
        self.assertEqual(
            intersect(Point(0, 0), Point(2, 2), Point(2, 2), Point(0, 0)), Point(0, 0))

    def test_when_lines_are_overlapping_segments_then_return_intersection_point_with_smallest_x(self):
        self.assertEqual(
            intersect(Point(0, 0), Point(2, 2), Point(2, 2), Point(1, 1)), Point(1, 1))

    def test_when_lines_intersect_then_return_intersection_point(self):
        self.assertEqual(
            intersect(Point(0, 0), Point(2, 2), Point(0, 2), Point(2, 0)), Point(1, 1))


if __name__ == '__main__':
    unittest.main()
