"""
1986. Minimum Number of Work Sessions to Finish the Tasks https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/

There are n tasks assigned to you. The task times are represented as an integer array tasks of length n,
where the ith task takes tasks[i] hours to finish.
A work session is when you work for at most sessionTime consecutive hours and then take a break.
You should finish the given tasks in a way that satisfies the following conditions:
If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime,
return the minimum number of work sessions needed to finish all the tasks following the conditions above.
The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].
Example 1:
Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
Example 2:
Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
Example 3:
Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.
Constraints:
n == tasks.length
1 <= n <= 14
1 <= tasks[i] <= 10
max(tasks[i]) <= sessionTime <= 15

SOLUTION
dp[bitmask] = (min sessions needed, min hours of tasks in the last session)
Bitmask represents the subset of tasks selected from n tasks.
Go through all tasks who belong to S and optimally choose the last task i who enters the session.
Each such choice yields a subproblem for a smaller subset of tasks.
Time O(2^N * N): better than brute force all permutations (N!)
Space O(2^N)
References
- CSES competitive programming handbook p.103
- https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/
- https://docs.particle.io/cards/firmware/language-syntax/bitwise-operators/
"""

from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        pow2n = 1 << n
        # Base case 1: n sessions required in worst case scenario
        dp = [(n, 0) for _ in range(pow2n)]
        # Base case 2: 1 session required even if no task selected
        dp[0] = (1, 0)
        for s in range(1, pow2n):
            for i in range(n):
                # i-th task is present in subset
                if s & (1 << i):
                    # get prev computation for subset less i-th task
                    # caret symbol is bitwise XOR operator
                    c, w = dp[s ^ (1 << i)]
                    if w + tasks[i] > sessionTime:  # new session for i-th person
                        c += 1
                        w = tasks[i]
                    else:
                        w += tasks[i]
                    dp[s] = min(dp[s], (c, w))
        return dp[pow2n - 1][0]  # 2^n-1: all tasks selected
