"""
18. 4Sum https://leetcode.com/problems/4sum/description/

Given an array nums of n integers,
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

SOLUTION
Break down the sum x = a + b + c + d into sum of two pairs.
1st pass
- Get first pair sum by looping all combinations
- Not permutations because sum is associative
2nd pass
- Find the 2nd pair (complement of the 1st pair sum)
Time O(N^2)
Space O(N^2): bec we have to store positions, otherwise O(1).
References
- https://usaco.guide/problems/cses-1642-sum-of-four-values/solution
"""

from collections import defaultdict
from typing import List, Set, Tuple


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # Corner case 1: less than 4
        if n < 4:
            return []
        # Corner case 2: all elements are the same
        all_same = True
        prev = nums[0]
        for i in range(1, n):
            if nums[i] != prev:
                all_same = False
                break
            prev = nums[i]
        if all_same and target == nums[0] * 4:
            return [[nums[0]] * 4]
        res: Set[Tuple[int, ...]] = set()
        # map of pair sum to List of positions (i, j)
        mp = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = nums[i] + nums[j]
                mp[x].append((i, j))
        for x, xpos in mp.items():
            y = target - x
            if y in mp:
                ypos = mp[y]
                for a, b in xpos:
                    for c, d in ypos:
                        if a != c and a != d and b != c and b != d:
                            r = [nums[a], nums[b], nums[c], nums[d]]
                            r.sort()
                            res.add(tuple(r))
        return [list(r) for r in res]
