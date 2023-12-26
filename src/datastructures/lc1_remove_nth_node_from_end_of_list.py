"""
19. Remove Nth Node From End of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
Follow up: Could you do this in one pass?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head  # p1 points to the node for removal
        p2 = head  # p2 is n steps ahead
        for _ in range(n):
            p2 = p2.next
        if p2 is None:
            return head.next  # type: ignore[no-any-return]
        while p2 is not None:
            if p1.next is not None and p2.next is None:
                p1.next = p1.next.next
            p1 = p1.next
            p2 = p2.next
        return head
