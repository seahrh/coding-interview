"""
57. Insert Interval https://leetcode.com/problems/insert-interval/description/

You are given an array of non-overlapping intervals `intervals`
where intervals[i] = [starti, endi] represent the start and the end of the ith interval and
intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

from bisect import bisect_left
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        def is_overlap(a: List[int], b: List[int]) -> bool:
            return a[0] <= b[1] and b[0] <= a[1]

        def merge_intervals(a: List[int], b: List[int]) -> List[int]:
            return [min(a[0], b[0]), max(a[1], b[1])]

        i = bisect_left(intervals, newInterval)
        j = i - 1
        lef = []
        while j >= 0 and is_overlap(intervals[j], newInterval):
            lef.append(intervals[j])
            j -= 1
        x = j + 1
        rig = []
        j = i
        while j < len(intervals) and is_overlap(intervals[j], newInterval):
            rig.append(intervals[j])
            j += 1
        y = j
        overlaps = lef + rig
        # print(f"overlaps={overlaps}")
        z = newInterval
        for i in range(len(overlaps)):
            z = merge_intervals(z, overlaps[i])
        return intervals[:x] + [z] + intervals[y:]
