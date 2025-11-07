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
Problem Recap
You’re given a list of bar heights. Each bar is 1 unit wide. How much water can collect between the bars after it rains?

Key Insight
Water trapped at any position depends on:
The tallest bar to the left (left_max)
The tallest bar to the right (right_max)
Trapped water = min(left_max, right_max) - height at position

Two-Pointer Approach (O(N) Time, O(1) Space)
Initialize two pointers: left at start, right at end
Track the max heights seen so far: left_max (for left side), right_max (for right side)
Move pointers towards each other: Always move the pointer at the shorter bar.
If height[left] < height[right], water at left is limited by left_max.
Otherwise, water at right is limited by right_max.
For each pointer move:
If the current bar is a new max, update left_max or right_max.
Else, add trapped water at that position (max_so_far - height).
Move pointer inward. Repeat until pointers cross.

Why Does This Work?
You only trap water where a lower bar is surrounded by higher bars.
By always advancing the shorter bar, we are “filling up” just enough for that side—never overestimating.

Time O(N): No additional lists, and every element visited at most once.
Space O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left, right = 0, n - 1  # Two pointers
        left_max, right_max = 0, 0  # Track highest bars to left/right
        water = 0
        while left < right:
            if height[left] < height[right]:
                # Water trapped at left depends on left_max
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                # Water trapped at right depends on right_max
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
