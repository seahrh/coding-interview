"""
4. Median of Two Sorted Arrays https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

SOLUTION
Binary search on 2 arrays: in each array, determine the last element of the left partition.
If total length is odd, then median is the tail of left partition.
If total length is even, then median is the average of (left partition tail, right partition head).
Time O(lg (M+N))
Space O(1)
References
- https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/4070500/99-journey-from-brute-force-to-most-optimized-three-approaches-easy-to-understand/
- https://www.youtube.com/watch?v=LPFhl65R7ww
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:  # Ensure 1st array is the smaller array
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        # Left partition size: Last element(s) of left partition is the median
        # Since len(nums1)<=len(nums2), increase the length of nums1 by 1.
        # This allows the whole of nums1 to be left partition if lo=hi=n1 (last index)
        left = (n1 + n2 + 1) // 2
        # 1st array has its length increased by 1, so hi=n1 (not n1-1)
        lo, hi = 0, n1
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = left - mid1
            # tail of left partition, head of right partition
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            # Partition is correct, found median
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2.0
            if l1 > r2:
                hi = mid1 - 1
                continue
            lo = mid1 + 1
        return 0  # If the code reaches here, the input arrays were not sorted.
