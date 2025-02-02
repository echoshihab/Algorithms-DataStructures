"""
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Constraints:

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""


from typing import Optional
from Problems.balancedBinaryTree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = None
        self.curr_max = None
            
        self.calculate_max(root)
        return self.max_val
        
    def calculate_max(self, node):
        if not node:
            self.max_val = max(self.max_val, self.curr_max)
            return
        if not self.max_val:
            self.max_val = node.val
            self.curr_max = node.val
        elif (node.val + self.curr_max) < node.val :
            self.max_val = max(self.max_val, self.curr_max)
            self.curr_max = node.val
        else:
            self.curr_max = self.max_val + node.val

        self.calculate_max(node.left)
        self.calculate_max(node.right)
