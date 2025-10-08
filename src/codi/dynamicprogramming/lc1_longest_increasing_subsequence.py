"""
300. Longest Increasing Subsequence https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

SOLUTION
dp[i] = smallest ending value (tail) of an increasing subsequence of length i+1,
For each item x in the array, do one of the following:
(1) if x is larger than all tails, append it, increase the size by 1
(2) if dp[i-1] < x <= dp[i], update dp[i].
Find index i with binary search on dp array (sorted).
Final answer is the length of dp array.
In this task we were asked to find the longest strictly increasing subsequence.
To find the longest increasing subsequence where we allow consecutive equal values,
change lower_bound to upper_bound.
Time O(N lg N): binary search in the loop
Space O(N): memo array

References
- https://codeforces.com/blog/entry/70018
- https://leetcode.com/problems/longest-increasing-subsequence/solutions/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation/
"""

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[int] = []
        for i in nums:
            j = bisect_left(dp, i)
            if j == len(dp):
                dp.append(i)
                continue
            dp[j] = i
        return len(dp)
