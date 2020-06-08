"""
QUICKSORT
=============
Quicksort worst case is slower than mergesort, O(N^2) vs O(N lg N).
Worst case: array is already sorted, or poor choice of pivot.
Quicksort takes less space than mergesort, O(lg N) vs O(N).
In-place sort, hence not a stable sort like mergesort.
"""
from abc import ABCMeta, abstractmethod
from typing import TypeVar, List, Any, Callable, Optional, Tuple


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __le__(self, other: Any) -> bool:
        ...


T = TypeVar("T", bound=Comparable)


def lomuto_partition(
    arr: List[T], lo: int, hi: int, pivot_fn: Callable
) -> Tuple[int, int]:
    """Divides the array into two partitions:
    Left partition contains all elements less than or equals the pivot, move to the left by swapping.
    Return the last index of the left partition, and the first index of the right partition.
    Picks the last element as the pivot.
    p is the final position of the pivot.
    """
    pivot_fn(arr, lo, hi)
    pivot = arr[hi]
    p = lo
    i = lo
    while i < hi:  # no need to cover the last element (pivot)
        if arr[i] <= pivot:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
        i += 1
    arr[p], arr[i] = arr[i], arr[p]
    return p - 1, p + 1  # exclude the pivot, else infinite recursion!


def hoare_partition(
    arr: List[T], lo: int, hi: int, pivot_fn: Callable
) -> Tuple[int, int]:
    # Return the last index of the left partition, and the first index of the right partition.
    # Hoare's scheme is more efficient than Lomuto's partition scheme because
    # it does three times fewer swaps on average,
    # and it creates efficient partitions even when all values are equal.
    # Like Lomuto, Hoare's partitioning scheme also degrades to O(n^2) for already sorted arrays.
    pivot_fn(arr, lo, hi)
    pivot = arr[hi]
    i = lo - 1
    j = hi + 1
    while True:
        # do-while loop forces cursor to move if all elements equal pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j, j + 1
        arr[i], arr[j] = arr[j], arr[i]


def median_of_three(arr: List[T], lo: int = 0, hi: Optional[int] = None) -> None:
    """Places median element in index hi."""
    if hi is None:
        hi = len(arr) - 1
    mid = int(lo / 2 + hi / 2)
    if arr[lo] <= arr[mid] <= arr[hi] or arr[hi] <= arr[mid] <= arr[lo]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        return
    if arr[mid] <= arr[lo] <= arr[hi] or arr[hi] <= arr[lo] <= arr[mid]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    # arr[hi] is the median; noop


def _quicksort(
    arr: List[T], lo: int, hi: int, partition_fn: Callable, pivot_fn: Callable
) -> None:
    # Base case: array of length one
    if lo >= hi:
        return
    left_tail, right_head = partition_fn(arr=arr, lo=lo, hi=hi, pivot_fn=pivot_fn)
    _quicksort(arr, lo, left_tail, partition_fn, pivot_fn)
    _quicksort(arr, right_head, hi, partition_fn, pivot_fn)


def quicksort(
    arr: List[T],
    partition_fn: Callable = lomuto_partition,
    pivot_fn: Callable = median_of_three,
) -> None:
    if arr is None or len(arr) == 0:
        raise ValueError("array must not be None or empty")
    _quicksort(arr, 0, len(arr) - 1, partition_fn, pivot_fn)
