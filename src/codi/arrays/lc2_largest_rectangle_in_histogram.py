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
Monotonic Increasing Stack
The stack stores indices of bars in non-decreasing order of height.
When we encounter a shorter bar, we compute rectangle areas for all bars that are taller and have just ended.
Why append 0 to heights?
Forces the algorithm to process and clear all remaining bars in the stack at the end, ensuring we check all potential rectangles.
Algorithm Process
Loop through each bar (including the appended 0):
If the current bar is higher or equal than the stack's top, push its index.
If it's lower, repeatedly pop bars from the stack and calculate areas using:
Height = the height of the popped bar.
Width = current index i minus the index after popping (if stack empty, width is full range).
Area Calculation
Treat each popped bar as the smallest in its window:
left bound: one past current stack top (or 0 if stack empty)
right bound: just before current bar (index i).
Update max_area whenever a bigger rectangle is found.

Time O(N): Each bar is pushed and popped once
Space O(N): In worst case, stack grows to full length

Real-World Significance: The technique is an efficient way to find range maxima
or solve "largest area under curve" problems in data, image analysis, or skyline/landscape scenarios.
References
- https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/995249/python-increasing-stack-explained/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add a 0-height bar to flush out the stack at the end.
        heights.append(0)
        st: List[int] = []
        res = 0
        for i, h in enumerate(heights):
            # Maintain a stack of indexes with increasing bar heights.
            # Stack grows as long as bar heights are increasing.
            # When hitting a smaller bar, repeatedly pop,
            # each time calculating area of a rectangle that ends just before index i
            # This ensures we check all rectangles that each bar could form as the smallest bar in its range.
            while st and heights[st[-1]] > h:
                # Pop the top. It's the tallest in this monotonic increasing 'window'.
                height = heights[st.pop()]
                # If stack is empty, width is i (from 0 to i-1).
                # Else, width is between the next top of stack and i-1.
                width = i if not st else i - st[-1] - 1
                res = max(res, height * width)
            st.append(i)
        # No need to remove the extra 0; it doesn't affect the answer.
        return res
