from typing import Iterable

# skip mypy check because open issue https://github.com/python/typing/issues/760


def argmin(elements: Iterable) -> int:
    """Returns first index of smallest element."""
    return min(enumerate(elements), key=lambda x: x[1])[0]  # type: ignore


def argmax(elements: Iterable) -> int:
    """Returns first index of largest element."""
    return max(enumerate(elements), key=lambda x: x[1])[0]  # type: ignore
