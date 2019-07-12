"""
We will be implementing some fundamental math, representing integers as Peano numbers
using an immutable Num class where each list represents a positive integer.

0 ↔ None
1 ↔ Num(None)
2 ↔ Num(Num(None))
3 ↔ Num(Num(Num(None)))
"""


class Num:
    """Given class definition - do not change!"""
    def __init__(self, prev):
        self._prev = prev

    @property
    def prev(self):
        return self._prev

    def __eq__(self, other):
        if not isinstance(other, Num):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self._prev == other._prev


def to_int(num):
    if num is None:
        return 0
    n = 1
    curr = num
    while curr.prev is not None:
        n += 1
        curr = curr.prev
    return n


def from_int(value):
    if value == 0:
        return None
    res = Num(None)
    for i in range(1, value):
        res = Num(res)
    return res


def add(a, b):
    res = None
    while a is not None:
        res = Num(res)
        a = a.prev
    while b is not None:
        res = Num(res)
        b = b.prev
    return res


def subtract(a, b):
    res = a
    while b is not None:
        if res is None:
            break
        res = res.prev
        b = b.prev
    return res
