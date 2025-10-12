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
Time O(N)
three steps:
1. Find the middle of the list (using the slow/fast pointer method).
2. Reverse the second half of the list.
3. Merge the two halves alternately.
Space O(1)
References
- https://leetcode.com/problems/reorder-list/solutions/801883/python-3-steps-to-success-explained/
"""

from typing import Optional

from codi.linkedlists import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        # Step 1: Find the middle of the list
        p1: Optional[ListNode] = head
        p2: Optional[ListNode] = head
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        # Second half is in the region after middle!
        mid = p1.next
        # Step 2: Reverse the second half of the list
        curr = mid
        prev = None
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # Truncate the first half of the list!
        p1.next = None
        # Step 3: Merge the two halves alternately
        p2 = prev
        p1 = head
        while p1 is not None and p2 is not None:
            n1 = p1.next
            n2 = p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
