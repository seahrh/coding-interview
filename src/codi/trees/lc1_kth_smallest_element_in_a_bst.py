"""
230. Kth Smallest Element in a BST https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
and you need to find the kth smallest frequently, how would you optimize?

SOLUTION
Inorder
Time O(N)
Space O(H): depth of recursion stack

Further Optimization for Frequent Modification (Follow-Up)
Augment TreeNodes with left_count:
Store the number of nodes in each node's left subtree.
During kth smallest search:
Compare k with left_count + 1 at each node:
k <= left_count → go left.
k == left_count + 1 → return node.
k > left_count + 1 → go right with k updated (k - left_count - 1).
Benefit: O(log n) for balanced trees, as you narrow down immediately—ideal for frequent queries and updates.
"""

from typing import Optional

from codi.trees import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1

        def inorder(root: Optional[TreeNode]) -> None:
            nonlocal res, k  # binding to variables outside the nested function
            if root is None:
                return
            inorder(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            inorder(root.right)

        inorder(root)
        return res


class TreeNodeAugmented:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNodeAugmented] = None
        self.right: Optional[TreeNodeAugmented] = None
        self.left_count: int = 0  # Number of nodes in left subtree


def insert(root: TreeNodeAugmented, val: int) -> TreeNodeAugmented:
    if not root:
        return TreeNodeAugmented(val)
    if val < root.val:
        root.left = insert(root.left, val)  # type: ignore[arg-type]
        root.left_count += 1  # Update left_count on insertion
    else:
        root.right = insert(root.right, val)  # type: ignore[arg-type]
    return root


# Delete Function
# (For brevity, not shown—but you'd also need to update left_count on deletions. Ask if you need this!)


def kth_smallest(root: TreeNodeAugmented, k: int) -> int:
    """
    Returns the kth smallest element in the BST (1-indexed).
    Assumes left_count is correctly updated on insert or delete.
    """
    node: Optional[TreeNodeAugmented] = root
    while node:
        if k <= node.left_count:
            node = node.left
        elif k == node.left_count + 1:
            return node.val
        else:
            k = k - node.left_count - 1
            node = node.right
    return -1  # Not found (should not happen if k is valid)
