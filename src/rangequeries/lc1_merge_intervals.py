"""
56. Merge Intervals https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

SOLUTION
References
- https://www.techinterviewhandbook.org/algorithms/interval/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlap(a: List[int], b: List[int]) -> bool:
            return a[0] <= b[1] and b[0] <= a[1]

        def merge_intervals(a: List[int], b: List[int]) -> List[int]:
            return [min(a[0], b[0]), max(a[1], b[1])]

        if len(intervals) == 1:
            return intervals
        intervals.sort()
        st: List[List[int]] = []
        for i in range(1, len(intervals)):
            a = intervals[i - 1]
            if len(st) != 0:
                a = st.pop()
            b = intervals[i]
            if is_overlap(a, b):
                st.append(merge_intervals(a, b))
                continue
            st.append(a)
            st.append(b)
        return st
