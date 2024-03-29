"""
876. Middle of the Linked List https://leetcode.com/problems/middle-of-the-linked-list/description/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

SOLUTION
Walk the linked list with 2 pointers: one fast and one slow.
Time O(N)
Space O(1)
"""
from typing import Optional

from codi.datastructures import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        while p2 is not None:
            if p2.next is None:
                break
            p1 = p1.next
            p2 = p2.next.next
        return p1
