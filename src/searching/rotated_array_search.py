"""
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.

Return the index of the found element, so assume no duplicates.

EXAMPLE
Input find 5 in {15, 16, 19, 20, 25, 1, 3,4,5,7,10, 14}
Output 8 (the index of 5 in the array)

(10.3, p410)
"""


def find(arr, key):
    """Modified version of binary search: one half of the array must be already sorted.
    Therefore check the sorted half to decide whether to search the left or right half.
    This takes O(lg n) time and O(1) space.
    """
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)
        if key == arr[mid]:
            return mid
        # left partition is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= key < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right partition is sorted
            if arr[mid] < key <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# Find index_of_min element in a sorted but rotated array.


def index_of_min(arr):
    """Look for min in the unsorted partition.
    This takes O(lg n) time and O(1) space.
    """
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    lo = 0
    hi = len(arr) - 1
    while arr[lo] > arr[hi]:
        mid = int(lo / 2 + hi / 2)
        if arr[lo] <= arr[mid]:  # right partition is unsorted
            lo = mid + 1  # offset required to avoid infinite loop
        else:  # left partition is unsorted
            hi = mid
    return lo
