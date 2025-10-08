"""
826. Most Profit Assigning Work https://leetcode.com/problems/most-profit-assigning-work/description/

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.
For example, if three workers attempt the same job that pays $1, then the total profit will be $3.
If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
Constraints:
n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105

SOLUTION
Sort jobs and workers by difficulty so we can use binary search to match worker to job.
dp[i] = highest profit from a single job considering the first i jobs sorted by difficulty.
Time O( (N+M)lg N + M lg M)
Space O(N)
"""

import sys
from bisect import bisect_right
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        n = len(profit)
        dp = [0] * (n + 1)
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], jobs[i - 1][1])
        res = 0
        worker.sort()
        for w in worker:
            # -1 bec jobs[:i] <= worker ability
            i = bisect_right(jobs, (w, sys.maxsize)) - 1
            # +1 bec dp is one-indexed
            res += dp[i + 1]
        return res
