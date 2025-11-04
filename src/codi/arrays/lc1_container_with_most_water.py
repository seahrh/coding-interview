"""
11. Container With Most Water https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

SOLUTION
Two pointers start at both ends of the x-axis.
To find a larger area when shrinking the width, compensate by looking for greater height.
Time O(N)
Space O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)
            if height[j] > height[i]:
                i += 1
                continue
            j -= 1
        return res
