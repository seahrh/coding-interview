"""
21. Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional

from codi.datastructures import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        h = None
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            h = list2
            list2 = list2.next
        elif list2 is None:
            h = list1
            list1 = list1.next
        elif list2.val <= list1.val:
            h = list2
            list2 = list2.next
        else:
            h = list1
            list1 = list1.next
        h.next = self.mergeTwoLists(list1, list2)
        return h
