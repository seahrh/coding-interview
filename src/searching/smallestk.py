"""
Smallest K: Design an algorithm to find the smallest K numbers in an array.

(17.14, p579)
Assumptions
- Input has duplicates.
- Modifying the array is allowed.

SOLUTION
1. Sorting (e.g. heapsort) takes O(n lg n) time and O(1) space.
2. Max heap takes O(n lg k) time and O(k) space.
3. Selection rank algorithm takes O(n) time and O(n) space because depth of call stack.
4. If range of values is known, hash table can be used where items are placed in their respective
interval buckets. This takes O(n) time and O(n) space.

"""
from collections import namedtuple


PartitionResult = namedtuple("PartitionResult", "left_size mid_size")


def _partition(arr, lo, hi, pivot):
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


def _rank(arr, k, lo, hi, pivot_fn):
    pivot = pivot_fn(arr, lo, hi)
    pr = _partition(arr, lo, hi, pivot)  # O(n) time
    # search portion of array: average O(lg n) time, worst O(n) time if poor choice of pivot.
    if k <= pr.left_size:
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


def rank(arr, k, pivot_fn=median_of_three):
    """Return the kth value from the array, where k starts from 1."""
    if not 1 <= k <= len(arr):
        raise ValueError("k must be in the range from 1 to array length, inclusive.")
    return _rank(arr, k, 0, len(arr) - 1, pivot_fn)


def smallest(arr, k):
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
    res = []
    for v in arr:
        if len(res) == k:
            break
        if v < threshold:
            res.append(v)
    # Any room left is for elements equal to the threshold. Copy them in.
    while len(res) < k:
        res.append(threshold)
    return res
