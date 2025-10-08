"""
84. Largest Rectangle in Histogram https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
Input: heights = [2,4]
Output: 4
Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104

SOLUTION
Monotonically Increasing Stack
References
- https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/995249/python-increasing-stack-explained/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st: List[int] = []
        res: int = 0
        for i, h in enumerate(
            heights + [0]
        ):  # append zero to pop all remaining elements in the stack
            while len(st) != 0 and heights[st[-1]] >= h:
                # popped out bar is left boundary, i is right boundary
                # we get a shorter bar as each bar is popped, but width increases
                H = heights[st.pop()]
                W = i if len(st) == 0 else i - 1 - st[-1]
                res = max(res, H * W)
            st.append(i)
        return res
