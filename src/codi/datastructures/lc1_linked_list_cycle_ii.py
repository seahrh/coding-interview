"""
142. Linked List Cycle II https://leetcode.com/problems/linked-list-cycle-ii/description/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
Follow up: Can you solve it using O(1) (i.e. constant) memory?

SOLUTION
Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
until they either meet or the fast pointer reaches the end of the list.
Slow takes x steps to reach the start node of the cycle, and another y steps to meet Fast in the cycle.
If Slow takes x+y steps to meet Fast, then Fast takes 2(x+y) steps.
Insight: Length of the cycle C is x+y because after entering the cycle, Slow takes y steps
and Fast takes x+y steps to meet Slow.
Time O(N)
Space O(1)
References
- explanation https://leetcode.com/problems/linked-list-cycle-ii/solutions/1701128/c-java-python-slow-and-fast-image-explanation-beginner-friendly/
- code https://leetcode.com/problems/linked-list-cycle-ii/solutions/3274329/clean-codes-full-explanation-floyd-s-cycle-finding-algorithm-c-java-python3/
"""

from typing import Optional

from codi.datastructures import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If the fast pointer reaches the end of the list without meeting the slow pointer,
        # there is no cycle in the linked list. Return None.
        return None
