"""
23. Merge k Sorted Lists https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:
Input: lists = []
Output: []
Example 3:
Input: lists = [[]]
Output: []
Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""
from heapq import heappop, heappush
from typing import List, Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        mnh: List[Tuple[int, int]] = []
        for i, x in enumerate(lists):
            if x is not None:
                heappush(mnh, (x.val, i))
        prev, head = None, None
        while len(mnh) != 0:
            _, i = heappop(mnh)
            curr = lists[i]
            if curr is not None:
                if head is None:
                    head = curr
                lists[i] = curr.next
                if curr.next is not None:
                    heappush(mnh, (curr.next.val, i))
            if prev is not None:
                prev.next = curr
            prev = curr
        return head
