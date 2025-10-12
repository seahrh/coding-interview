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

SOLUTION
To remove the Nth node from the end in one pass,
we can use the two-pointer technique (also known as the “fast and slow pointer” approach):
- Move a fast pointer ahead by n nodes.
- Then move both fast and slow pointers together until fast reaches the end.
- Now, the slow pointer is just before the node that needs to be removed.
- Adjust the pointers to skip that node.

We use a dummy node before the head to simplify edge cases (like removing the first node).
"""

from typing import Optional

from codi.linkedlists import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        # Move both until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        # Remove the nth node from end
        slow.next = slow.next.next
        return dummy.next
