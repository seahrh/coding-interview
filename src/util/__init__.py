from typing import Iterable, TypeVar


T = TypeVar("T")


def argmin(elements: Iterable[T]) -> int:
    """Returns first index of smallest element."""
    return min(enumerate(elements), key=lambda x: x[1])[0]


def argmax(elements: Iterable[T]) -> int:
    """Returns first index of largest element."""
    return max(enumerate(elements), key=lambda x: x[1])[0]
