"""
162. Find Peak Element https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

SOLUTION
Following corner cases give better idea about the problem.
If input array is sorted in strictly increasing order, the last element is always a peak element.
For example, 50 is peak element in {10, 20, 30, 40, 50}.
If the input array is sorted in strictly decreasing order, the first element is always a peak element.
100 is the peak element in {100, 80, 60, 50, 20}.
If all elements of input array are same, every element is a peak element.

Use Binary Search to find the peak in O(lg N) time.
Check if the middle element is the peak element or not.
If the middle element is not the peak,
then check if the element on the right is greater than the middle element,
there is always a peak element on the right side.
If the element on the left side is greater than the middle element
then there is always a peak element on the left side.

References
- https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
"""

from typing import List


class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = int(lo / 2 + hi / 2)
            smaller_than_left = mid - 1 >= lo and arr[mid] < arr[mid - 1]
            smaller_than_right = mid + 1 <= hi and arr[mid] < arr[mid + 1]
            if not smaller_than_left and not smaller_than_right:
                return mid
            if smaller_than_left:  # there is always a peak on the left
                hi = mid - 1
                continue
            # there is always a peak on the right
            lo = mid + 1
        raise ValueError("array must not be empty")
