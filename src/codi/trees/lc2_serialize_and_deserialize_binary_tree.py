"""
297. Serialize and Deserialize Binary Tree https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

SOLUTION
Serialization (Tree → String)
Idea: Use pre-order traversal (node, left, right).
For every node:
Add its value to a list.
For None children, add a special marker (here, #).
Flatten the list into a space-separated string.

Deserialization (String → Tree)
Idea: Reverse process.
Read the string, split by spaces, and walk through the values:
For every value:
If it’s #, return None.
Otherwise, create a new node.
Recursively build its left and right children.

Why Pre-order and Mark Nulls?
Reconstructing the exact tree shape requires knowing where the None nodes are.
Pre-order ensures you always know at each step whether a node exists and can reliably build both children.
Adding null markers makes your algorithm robust even for sparse or unbalanced trees.

Complexity (N = number of nodes)
Serialize: Preorder DFS, Time O(N), Space O(N), node values and mark # as null
Deserialize: Preorder DFS, Time O(N), Space O(N), read values in order and rebuild
Both time and space are linear, as we process each node once and store all values including Nulls.

References
- https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/74259/recursive-preorder-python-and-c-o-n/
"""

from typing import List, Optional

from codi.trees import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using pre-order traversal."""
        vals: List[str] = []

        def dfs(node):
            if not node:
                vals.append("#")  # Use '#' as a null marker
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return " ".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        vals = iter(data.split())

        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
