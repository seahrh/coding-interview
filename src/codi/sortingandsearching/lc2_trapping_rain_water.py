"""
42. Trapping Rain Water https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

SOLUTION
Two pointers: max height on left side, max height on right side.
Time O(N)
Space O(1)
References
- comments https://leetcode.com/problems/trapping-rain-water/solutions/3401992/100-detailed-explaination-with-pictures-in-c-java-python-two-pointers/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmx, rmx, res = 0, 0, 0
        lo, hi = 0, n - 1
        while lo <= hi:
            # count trapped water on left side of the peak
            if height[lo] <= height[hi]:
                lmx = max(lmx, height[lo])
                res += lmx - height[lo]
                lo += 1
                continue
            # count trapped water on right side of the peak
            rmx = max(rmx, height[hi])
            res += rmx - height[hi]
            hi -= 1
        return res
