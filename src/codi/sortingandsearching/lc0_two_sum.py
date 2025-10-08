"""
1. Two Sum https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple


class Solution:
    def twoSumSorting(self, nums: List[int], target: int) -> List[int]:
        """
        Time O(N lg N)
        Space O(N)
        """
        # In the Pair, 1st element is the value, 2nd element is the original array index.
        ar: List[Tuple[int, int]] = [(x, i) for i, x in enumerate(nums)]
        ar.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sm = ar[i][0] + ar[j][0]
            if sm == target:
                break
            if sm > target:
                j -= 1
                continue
            if sm < target:
                i += 1
        return [ar[i][1], ar[j][1]]


def two_sum(arr: List[int], target: int) -> Set[Tuple[int, int]]:
    """Returns a set of pairs (therefore no duplicate pairs).
    Builds a hash table where key is a complement and value is the number of times
    that this complement can be added to a valid pair.
    Requires only one pass because addition is commutative
    i.e. order of operands does not matter.

    This takes O(n) time and O(n) space.
    """
    res: Set[Tuple[int, int]] = set()
    unpaired_count: DefaultDict[int, int] = defaultdict(int)
    for a in arr:
        complement = target - a
        if unpaired_count[a] > 0:  # current value matches the complement
            if a < complement:
                res.add((a, complement))
            else:
                res.add((complement, a))
            unpaired_count[a] -= 1
            continue
        unpaired_count[complement] += 1
    return res
