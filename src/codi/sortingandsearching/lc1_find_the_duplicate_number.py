"""
287. Find the Duplicate Number https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

SOLUTION - similar to Linked List Cycle II
Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
until they either meet or the fast pointer reaches the end of the list.
Slow takes x steps to reach the start node of the cycle, and another y steps to meet Fast in the cycle.
If Slow takes x+y steps to meet Fast, then Fast takes 2(x+y) steps.
Insight: Length of the cycle C is x+y because after entering the cycle, Slow takes y steps
and Fast takes x+y steps to meet Slow.

Special LL node where `next` pointer is the array element at index i.
Head node has `next` pointing to ar[0].
If there is no cycle (no duplicate), then tail node has `next` pointing to ar[n] where n is IndexOutOfBounds.
If cycle is present (has duplicate), then ar[n] is within bounds because len(ar)=n+1
Time O(N)
Space O(1)
References
- https://leetcode.com/problems/find-the-duplicate-number/solutions/1892921/9-approaches-count-hash-in-place-marked-sort-binary-search-bit-mask-fast-slow-pointers/
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        slow = fast = 0
        slow = nums[slow]  # do-while loop
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
