from typing import Iterable


def argmin(elements: Iterable):
    return min(enumerate(elements), key=lambda x: x[1])[0]


def argmax(elements: Iterable):
    return max(enumerate(elements), key=lambda x: x[1])[0]
