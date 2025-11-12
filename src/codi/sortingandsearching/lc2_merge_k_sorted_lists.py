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

SOLUTION
Approach: Min-Heap (Priority Queue)
Why a heap?
It allows us to efficiently find and pull out the smallest element among k sorted linked lists, each time in O(log k) time.
Steps Explained
1. Initialize the Heap
For each linked list, add the first node to the heap.
Each heap element is (node value, list index, node reference) to distinguish nodes even if they have the same value.
2. Building the Merged List
Use a dummy head node (makes the logic for linking straightforward).
While the heap isn't empty:
Pop the smallest node (by value).
Attach this node to the merged list.
If the popped node has a next node, push that onto the heap (from the same original list).
3. Final Output
The dummy head's next points to the sorted, merged list.

Time O(N lg K): Each node is pushed/popped once with heap (N is total number of nodes across all lists)
Space O(K): Heap contains up to K nodes at a time.
"""

from heapq import heappop, heappush
from typing import List, Optional, Tuple

from codi.linkedlists import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min-heap to keep track of the smallest node among the list heads
        # Each entry will be (node value, list index, node reference)
        heap: List[Tuple] = []
        # Step 1: Push the head of each non-empty list onto the heap
        for idx, node in enumerate(lists):
            if node is not None:
                # Store tuple: (value, index, node)
                heappush(heap, (node.val, idx, node))
        # Prepare a dummy head to simplify appending nodes
        dummy = ListNode(0)
        prev = dummy
        # Step 2: Pop the smallest node, append to result, push its next if available
        while len(heap) != 0:
            val, idx, node = heappop(heap)
            prev.next = node
            prev = prev.next
            # Move the pointer in the lists[idx] to the next node
            if node.next:
                heappush(heap, (node.next.val, idx, node.next))
        # Return the merged list starting after dummy node
        return dummy.next
