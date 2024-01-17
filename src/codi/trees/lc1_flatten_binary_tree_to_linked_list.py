"""
114. Flatten Binary Tree to Linked List https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class
where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:
Input: root = []
Output: []
Example 3:
Input: root = [0]
Output: [0]
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?

SOLUTION
"Inverse" postorder traversal (right, left, root): Build the linked list in reverse order.
After traversing right subtree, head points to the root of right subtree.
After traversing the rightmost leaf node in left subtree, set leaf.right=head of right subtree
After traversing left subtree, head points to the root of left subtree. Set root.right=head of left subtree
Time O(N)
Space O(N)

References
- comments https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/36977/my-short-post-order-traversal-java-solution-for-share/
"""
from codi.trees import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = None

        def dfs(root: TreeNode) -> None:
            nonlocal head

            if root is None:
                return
            dfs(root.right)
            dfs(root.left)
            root.right = head
            root.left = None
            head = root

        dfs(root)
