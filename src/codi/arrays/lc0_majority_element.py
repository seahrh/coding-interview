"""
169. Majority Element https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Constraints:
n == nums.length
1 <= n <= 5 * 104
-10^9 <= nums[i] <= 10^9
Follow-up: Could you solve the problem in linear time and in O(1) space?

SOLUTION
Moore Voting Algorithm works on the basis of the assumption
that the majority element occurs more than n/2 times in the array.
It guarantees that even if the count is reset to 0 by other elements,
the majority element will eventually regain the lead.
References
- https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate
