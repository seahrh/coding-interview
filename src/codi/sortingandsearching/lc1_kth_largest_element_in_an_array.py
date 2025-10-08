"""
215. Kth Largest Element in an Array https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Constraints:
1 <= k <= nums.length <= 105
-10^4 <= nums[i] <= 10^4

SOLUTION
1. Min-heap of k largest items, root is k-th largest item.
Time O(N lg K)
Space O(K)
References
- https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/3906260/100-3-approaches-video-heap-quickselect-sorting/
"""

from heapq import heapify, heappushpop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minh = list(nums[:k])
        heapify(minh)
        for i in range(k, len(nums)):
            if nums[i] > minh[0]:
                heappushpop(minh, nums[i])
        return minh[0]
