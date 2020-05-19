"""
Intersection: Given two straight line segments (represented as a start point and an end point)'
compute the point of intersection, if any.
(16.3, p475)
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def is_between(self, p1, p2):
        return min(p1.x, p2.x) <= self.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= self.y <= max(p1.y, p2.y)


class Line:
    def __init__(self, start, end):
        delta_y = end.y - start.y
        delta_x = end.x - start.x
        self.slope = delta_y / delta_x  # will be infinity when delta_x = 0
        self.intercept = end.y - self.slope * end.x


def intersect(start1, end1, start2, end2):
    """Return the intersection point of two lines, else return None.
    Ideas:
    For parallel lines to intercept (equal slope and y-intercept),
    they must be overlapping segments of the same infinite line.
    Intersection point is given by solving line equation 1 = line equation 2,
    m1 * x + c1 = m2 * x + c2
    x = (c2 - c1) / (m1 - m2)
    Additionally, the intersection must exist within the x-y boundaries of the two lines.
    """
    if start1.x > end1.x:
        tmp = end1
        end1 = start1
        start1 = tmp
    if start2.x > end2.x:
        tmp = end2
        end2 = start2
        start2 = tmp
    if start1.x > start2.x:
        tmp = start2
        start2 = start1
        start1 = tmp
        tmp = end2
        end2 = end1
        end1 = tmp
    l1 = Line(start1, end1)
    l2 = Line(start2, end2)
    if l1.slope == l2.slope:
        if l1.intercept == l2.intercept and start2.is_between(start1, end1):
            return start2
        return None
    x = (l2.intercept - l1.intercept) / (l1.slope - l2.slope)
    y = x * l1.slope + l1.intercept
    res = Point(x, y)
    if res.is_between(start1, end1) and res.is_between(start2, end2):
        return res
    return None
