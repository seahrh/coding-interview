"""
143. Reorder List https://leetcode.com/problems/reorder-list/description/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

SOLUTION
Time O(N): O(n) iterations to find middle, then O(n) iterations to reverse second half and finally,
O(n) iterations to merge lists.
Space O(1)
References
- https://leetcode.com/problems/reorder-list/solutions/801883/python-3-steps-to-success-explained/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        # step 1: find middle
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr is not None:
            nextt = curr.next
            curr.next = prev  # truncate the 2nd half
            prev = curr
            curr = nextt
        slow.next = None  # truncate the 1st half
        # step 3: merge lists
        h1, h2 = head, prev
        while h2 is not None:
            n1 = h1.next
            n2 = h2.next
            h1.next = h2
            h2.next = n1
            h1 = n1
            h2 = n2
