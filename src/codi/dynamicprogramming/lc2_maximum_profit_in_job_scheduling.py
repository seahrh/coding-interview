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
Bottom-up DP, dp[i] = max reward for considering the first i projects
Two choices: either do project i or give it up
Recurring relation: dp[i] = max(dp[i - 1], take project i)
Take project i = reward_i + dp[j]
where j is the nearest project on the left that ends <= start of project i
Time O(N lg N): sort projects, binary search in the loop
Space O(N): memo array
References
- https://www.youtube.com/watch?v=MJn3ogwsUbo
"""
from bisect import bisect_right
from typing import List, NamedTuple


class Job(NamedTuple):
    end: int
    start: int
    profit: int


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)
        jobs: List[Job] = []
        for i in range(n):
            jobs.append(Job(end=endTime[i], start=startTime[i], profit=profit[i]))
        jobs.sort()
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            ith = jobs[i - 1].profit
            start = jobs[i - 1].start
            # bisect_right or upper_bound: ar[lo:i]<=x
            # minus 1 bec we want the last job that ends <= start of job i
            # add 1 bec dp is one-indexed
            j = bisect_right(jobs, Job(end=start, start=start, profit=1)) - 1 + 1
            ith += dp[j]
            dp[i] = max(dp[i - 1], ith)
        return dp[n]
