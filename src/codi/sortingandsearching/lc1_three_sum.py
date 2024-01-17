"""
15. 3Sum https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

SOLUTION
Sort the array and run through all indices of a possible first element of a triplet.
For each possible first element, make a bi-directional sweep of the remaining part of the array.
Time O(N^2)
Space O(1)
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm == 0:
                    if nums[i] <= nums[j] <= nums[k]:
                        res.add((nums[i], nums[j], nums[k]))
                    elif nums[i] <= nums[k] <= nums[j]:
                        res.add((nums[i], nums[k], nums[j]))
                    elif nums[j] <= nums[i] <= nums[k]:
                        res.add((nums[j], nums[i], nums[k]))
                    elif nums[j] <= nums[k] <= nums[i]:
                        res.add((nums[j], nums[k], nums[i]))
                    elif nums[k] <= nums[i] <= nums[j]:
                        res.add((nums[k], nums[i], nums[j]))
                    elif nums[k] <= nums[j] <= nums[i]:
                        res.add((nums[k], nums[j], nums[i]))
                    j += 1
                    k -= 1
                    continue
                if sm < 0:
                    j += 1
                    continue
                k -= 1
        return list(res)  # type: ignore[arg-type]
