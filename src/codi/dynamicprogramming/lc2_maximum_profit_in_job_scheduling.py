"""
1235. Maximum Profit in Job Scheduling https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays,
return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.
Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

SOLUTION
Sort jobs by their ending time.
This makes it easier to identify compatible (non-overlapping) jobs, as earlier-ending jobs will be considered before later ones.
Bottom-up dynamic programming.
dp[i] tracks the maximum profit possible after considering the first i jobs.
Binary search with bisect_right.
For each job, find the last job that doesn't conflict with the current one.

Time O(N lg N): Sorting and binary search enable fast lookup of non-overlapping jobs
Space O(N): memo array
References
- https://www.youtube.com/watch?v=MJn3ogwsUbo
"""

from bisect import bisect_right
from typing import List, Tuple


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Combine the jobs into a single list of tuples and sort by end time.
        # (start, end, profit)
        jobs: List[Tuple] = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        # dp[i] will hold the max profit for the first i jobs.
        dp = [0] * (n + 1)
        # For binary search, we want a list of all end times
        ends = [job[1] for job in jobs]
        for i in range(1, n + 1):
            # Profits if we take the current job
            current_start, current_end, current_profit = jobs[i - 1]
            # Find the rightmost job that doesn't overlap using bisect_right.
            # bisect_right returns the insertion point to maintain sorted order.
            # It searches for current_start in the ends list.
            # The result j is the index where jobs[j].end <= current_start.
            # So the jobs before 'j' are compatible.
            j = bisect_right(ends, current_start)
            # Option 1: Don't take this job (dp[i - 1])
            # Option 2: Take this job: profit + best previous non-overlapping dp[j]
            dp[i] = max(dp[i - 1], current_profit + dp[j])
        return dp[n]
