"""
Find a peak element
=====================
Given an array of integers. Find a peak element in it.
An array element is a peak if it is NOT smaller than its neighbours.
For corner elements, we need to consider only one neighbour.

Example:
Input: array[]= {5, 10, 20, 15}
Output: 20
The element 20 has neighbours 10 and 15,
both of them are less than 20.

Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 or 90
The element 20 has neighbours 10 and 15, both of them are less than 20, similarly 90 has neighbours 23 and 67.

SOLUTION
Following corner cases give better idea about the problem.
If input array is sorted in strictly increasing order, the last element is always a peak element.
For example, 50 is peak element in {10, 20, 30, 40, 50}.
If the input array is sorted in strictly decreasing order, the first element is always a peak element.
100 is the peak element in {100, 80, 60, 50, 20}.
If all elements of input array are same, every element is a peak element.

Divide and Conquer can be used to find a peak in O(lg N) time.
The idea is based on the technique of Binary Search to check if the middle element is the peak element or not.

If the middle element is not the peak element,
then check if the element on the right side is greater than the middle element
then there is always a peak element on the right side.

If the element on the left side is greater than the middle element
then there is always a peak element on the left side.

See https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
"""
from typing import List


def peak(arr: List[int]) -> int:
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)
        smaller_than_left = mid - 1 >= lo and arr[mid] < arr[mid - 1]
        smaller_than_right = mid + 1 <= hi and arr[mid] < arr[mid + 1]
        if not smaller_than_left and not smaller_than_right:
            return mid
        # there is always a peak on the left
        if smaller_than_left:
            hi = mid - 1
            continue
        # there is always a peak on the right
        lo = mid + 1
    raise ValueError("array must not be empty")


def valley(arr: List[int]) -> int:
    """Valley element is NOT larger than its neighbours."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)
        larger_than_left = mid - 1 >= lo and arr[mid] > arr[mid - 1]
        larger_than_right = mid + 1 <= hi and arr[mid] > arr[mid + 1]
        if not larger_than_left and not larger_than_right:
            return mid
        # there is always a valley on the left
        if larger_than_left:
            hi = mid - 1
            continue
        # there is always a valley on the right
        lo = mid + 1
    raise ValueError("array must not be empty")
