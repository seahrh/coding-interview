"""
Problem Summary
Given a stream (or array) of numbers, compute the average of each consecutive subarray of length k.
Example:
Input: [1, 2, 3, 4, 5], k = 3
Output: [2, 3, 4]
((1+2+3)/3 = 2, (2+3+4)/3 = 3, (3+4+5)/3 = 4)

SOLUTION
Approach: Sliding Window
Instead of recalculating the sum for every window, keep a running sum.
Start by summing the first k items.
Slide the window: add the next number, subtract the one leaving the window.
For each window, append the average to result.

Time Complexity O(N)
Initialization: sum(nums[:k]) is O(k)
Sliding Window: Each iteration after the first takes O(1) (just add & subtract)
For an input array of length n, windows = n - k + 1
Space Complexity O(1)
"""

from typing import List


def moving_average(nums: List[int], k: int) -> List[float]:
    result: List[float] = []
    sm: int = 0
    # Do not slice to avoid space complexity O(K): sum(nums[:k])
    for i in range(k):
        sm += nums[i]
    result.append(sm / k)
    for i in range(k, len(nums)):
        # grow window from the right, shrink window from the left
        sm += nums[i] - nums[i - k]
        result.append(sm / k)
    return result
