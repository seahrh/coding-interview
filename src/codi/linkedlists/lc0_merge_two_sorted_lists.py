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

SOLUTION
Time Complexity
Both solutions must visit every node in both lists: each comparison and merge takes constant time.
So: O(m + n) for both.
Space Complexity
Recursive Solution: Each recursive call takes stack space.
In the worst case, you recurse through every node: O(m + n) additional space on the call stack.
Plus: the output list reuses existing nodes, so no extra heap allocation for nodes.
Iterative Solution
No recursion—just a few pointers (dummy, current, etc.).
You only use constant extra space: O(1), aside from the actual nodes of the final merged list.
"""

from typing import Optional

from codi.linkedlists import ListNode


class Solution:

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Iterative solution that has better space complexity O(1) vs. recursion."""
        dummy = ListNode()
        n1 = list1
        n2 = list2
        curr = dummy
        while n1 is not None and n2 is not None:
            if n1.val <= n2.val:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next
        if n1 is None and n2 is not None:
            curr.next = n2
        if n2 is None and n1 is not None:
            curr.next = n1
        return dummy.next

    def mergeTwoListsRecursion(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
