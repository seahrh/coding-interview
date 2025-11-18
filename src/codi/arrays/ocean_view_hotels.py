"""
Problem Statement
Input: An array heights where heights[i] represents the height of hotel i. The ocean is to the right.
Output: Return the indices of hotels with ocean view—meaning no hotel to their right is taller (or equal).
Intuitive Solution
Scan the array from right to left. Track the maximum height seen so far;
if the current hotel is taller than this max, it has an ocean view.

SOLUTION
Start at the end of the array (rightmost hotel always has ocean view).
Update the max seen so far after each hotel.
If current hotel is > max, it’s added to the result.

Time O(N): single pass from right to left
Space O(1): do not count output data structure
"""

from typing import List


def ocean_view_hotels(heights: List[int]) -> List[int]:
    n = len(heights)
    result: List[int] = []
    max_height = float("-inf")
    for i in range(n - 1, -1, -1):
        if heights[i] > max_height:
            result.append(i)
            max_height = heights[i]
    result.reverse()  # Return indices in left-to-right order
    return result
