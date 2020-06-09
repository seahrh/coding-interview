"""
Smallest K: Design an algorithm to find the smallest K numbers in an array.

(17.14, p579)
Assumptions
- Input has duplicates.
- Modifying the array is allowed.

SOLUTION
1. Sorting (e.g. heapsort) takes O(N lg N) time and O(1) space.
2. Heap takes O(N lg K) time and O(K) space. (although K can equal N)
3. Selection rank algorithm takes O(N) time and O(N) space because recursive call stack.
4. If range of values is known, hash table can be used where items are placed in their respective
interval buckets. This takes O(N) time and O(N) space.
"""
from typing import NamedTuple, List, Callable


class PartitionResult(NamedTuple):
    left_size: int
    mid_size: int


def _partition(arr: List[int], lo: int, hi: int, pivot: int) -> PartitionResult:
    """Divide the array into three partitions: less than the pivot, equal to the pivot
    and greater than the pivot.
    """
    head = lo  # head of middle partition
    tail = hi  # tail of middle partition
    i = lo  # current item for evaluation
    while i <= tail:  # cover all items in lo..hi range inclusive
        if arr[i] < pivot:
            # grow left partition
            arr[head], arr[i] = arr[i], arr[head]
            i += 1
            head += 1
            continue
        if arr[i] > pivot:
            # right can have any value, swap them so that new right is larger than pivot.
            # grow right partition
            arr[tail], arr[i] = arr[i], arr[tail]
            tail -= 1
            continue
        # element i equals pivot
        i += 1
    return PartitionResult(left_size=head - lo, mid_size=tail - head + 1)


def median_of_three(arr: List[int], lo: int, hi: int) -> int:
    """Get the approximate median of three items in the subarray specified by `lo` and `hi` indices, inclusive.
    Given only one distinct item, return itself.
    Given two distinct items, return either item.
    Given three distinct items, return the one in the middle.
    """
    mid = int(lo / 2 + hi / 2)
    if arr[lo] <= arr[mid] <= arr[hi] or arr[hi] <= arr[mid] <= arr[lo]:
        return arr[mid]
    if arr[mid] <= arr[lo] <= arr[hi] or arr[hi] <= arr[lo] <= arr[mid]:
        return arr[lo]
    return arr[hi]


def _rank(arr: List[int], k: int, lo: int, hi: int, pivot_fn: Callable) -> int:
    pivot: int = pivot_fn(arr, lo, hi)
    pr = _partition(arr, lo, hi, pivot)  # O(n) time
    # search portion of array: average O(lg n) time, worst O(n) time if poor choice of pivot.
    if k <= pr.left_size:
        # lo + pr.left_size - 1 because first element lo is already included.
        return _rank(arr, k, lo, lo + pr.left_size - 1, pivot_fn)
    if k <= pr.left_size + pr.mid_size:
        return pivot  # middle partition contains only pivot values
    return _rank(
        arr,
        k=k - pr.left_size - pr.mid_size,
        lo=lo + pr.left_size + pr.mid_size,
        hi=hi,
        pivot_fn=pivot_fn,
    )


def rank(arr: List[int], k: int, pivot_fn: Callable = median_of_three) -> int:
    """Return the kth value from the array, where k starts from 1."""
    if not 1 <= k <= len(arr):
        raise ValueError("k must be in the range from 1 to array length, inclusive.")
    return _rank(arr, k, 0, len(arr) - 1, pivot_fn)


def smallest(arr: List[int], k: int) -> List[int]:
    """
    Since there are duplicates, there could be more than k items that are less than
    or equals to the kth item. First, copy only the items that are less than the kth item,
    then fill up the remaining space with the kth item.

    :param arr:
    :param k: k in the range from 1 to array length, inclusive.
    :return: array containing k smallest items
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k must be in the range from 1 to array length, inclusive.")
    threshold = rank(arr, k)
    res: List[int] = []
    for v in arr:
        if len(res) == k:
            break
        if v < threshold:
            res.append(v)
    # Any room left is for elements equal to the threshold. Copy them in.
    while len(res) < k:
        res.append(threshold)
    return res
