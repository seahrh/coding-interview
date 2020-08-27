"""
Given an array of integers,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max element of each sliding window.
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

SOLUTION
1. Maintain the window in a self balancing BST. Insert, delete, find max in O(lg N) time.
Time O(N lg N)
Space O(N)

2. A linear time solution exists.
Doubly linked list stores the index of useful elements of the current window.
An element is useful if it is in current window and is **greater than the new element on the right**.
If there is a larger element on the right, any smaller element in the list cannot be the solution so discard them.
Hence, the head of the list is always the maximum element.
Array index to check elements that do not belong to the current window. Remove them from the head of the list.
Time O(N): every element is pushed or popped from the list at most once.
Space O(N)

See
- https://leetcode.com/problems/sliding-window-maximum/
- https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""
from collections import deque
from typing import List, Deque


def solve(k: int, arr: List[int]) -> List[int]:
    res: List[int] = []
    q: Deque[int] = deque()
    # initialize first window
    for i in range(k):
        # discard smaller elements in the list
        while len(q) != 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    res.append(arr[q[0]])
    # i is the tail of the window
    for i in range(k, len(arr)):
        # discard elements no longer in the window
        while len(q) != 0 and q[0] <= i - k:
            q.popleft()
        # discard smaller elements in the list
        while len(q) != 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
        res.append(arr[q[0]])
    return res
