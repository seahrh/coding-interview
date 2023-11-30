"""
MERGESORT
============
Mergesort takes more space than quicksort, O(N) vs O(lg N).
Stable sort (not in-place)
"""
from abc import ABCMeta, abstractmethod
from typing import Any, List, TypeVar


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __le__(self, other: Any) -> bool:
        ...


T = TypeVar("T", bound=Comparable)


def _merge(left: List[T], right: List[T], arr: List[T]) -> None:
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergesort(arr: List[T]) -> None:
    # Base case: empty array or array of length 1
    if len(arr) < 2:
        return
    mid = int(len(arr) / 2)
    left = list(arr[:mid])
    right = list(arr[mid:])
    mergesort(left)
    mergesort(right)
    _merge(left, right, arr)
