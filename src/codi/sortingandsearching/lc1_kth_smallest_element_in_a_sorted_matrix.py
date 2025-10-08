"""
378. Kth Smallest Element in a Sorted Matrix https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).
Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
Follow up: Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?

SOLUTION
Nested heap (heap of heaps where each row is a heap)
Preserve the nested heap after the root matrix[0][0] is popped k times.
Time O(N^2): N^2 + K lg N
Space O(1): heapify in-place
References
- https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/4213390/python-solution-beating-99-7-memory-heapify-the-whole-matrix-inplace/
"""

from heapq import heapify, heappop, heapreplace
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # heapify each row
        for i in range(len(matrix)):
            heapify(matrix[i])
        # heap of heaps
        heapify(matrix)
        for _ in range(k):
            res = matrix[0][0]
            heappop(matrix[0])
            if len(matrix[0]) == 0:
                heappop(matrix)
            # nested heap: restore heap properties!
            # heappop() + heappush() is O(logN + logN)
            # heappushpop is wrong because the order of ops is wrong (push then pop)
            # not using heapq.heapify() because it is O(N)
            # heapreplace: Pop and return the smallest item from the heap,
            # and also push the new item. The heap size doesn’t change.
            if len(matrix) != 0:
                head = matrix[0]
                heapreplace(matrix, head)
        return res
