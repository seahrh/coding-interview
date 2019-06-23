"""
Smallest K: Design an algorithm to find the smallest K numbers in an array.

(17.14, p579)
Assumptions
- Input has duplicates.
- Modifying the array is allowed.

SOLUTION
1. Sorting (e.g. heapsort) takes O(n lg n) time and O(1) space.
2. Max heap takes O(n lg k) time and O(k) space.
3. Median selection algorithm takes O(n) time.
"""
from collections import namedtuple


PartitionResult = namedtuple('PartitionResult', 'left_size mid_size')


def _partition(arr, lo, hi, pivot):
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
        if arr[i] == pivot:
            i += 1
    return PartitionResult(left_size=head - lo, mid_size=tail - head + 1)


def median_of_three(arr, lo, hi):
    """Get the approximate median of three items
    in the subarray specified by `lo` and `hi` indices, inclusive.
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
