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
We are merging overlapping intervals — whenever two intervals overlap,
we merge them into a single one that covers both ranges.
If we sort by start time, any overlapping intervals must be adjacent.
Time O(N lg N)
Space O(1), if the result list is ignored.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1. Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        # Step 2. Compare each interval with the last merged one
        for a, b in intervals[1:]:
            c, d = res[-1][0], res[-1][1]  # noqa: F841
            if a <= d:
                res[-1][1] = max(b, d)
            else:
                res.append([a, b])
        return res
