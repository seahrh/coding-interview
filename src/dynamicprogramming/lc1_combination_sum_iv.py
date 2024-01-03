"""
377. Combination Sum IV https://leetcode.com/problems/combination-sum-iv/description/

Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.
Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:
Input: nums = [9], target = 3
Output: 0
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

SOLUTION
dp[i] = number of ways to make sum i
Loop over the possibilities for last coin added (all coins <= current target).
There are dp[x-v] ways to make x, when adding a coin with value v **last**.
Time O(N lg N + X lg N)
Space O(X): memo array
"""
from bisect import bisect_right
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        # Base case: all the coins that equals target
        for i in range(len(nums)):
            if nums[i] > target:
                break
            dp[nums[i]] = 1
        # start loop after 1st coin
        for i in range(nums[0] + 1, target + 1):
            # get all coins <= current target
            hi = bisect_right(nums, i)
            for j in range(hi):
                dp[i] += dp[i - nums[j]]
        return dp[target]
