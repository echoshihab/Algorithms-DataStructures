"""
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Constraints:

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

from typing import Optional
from Problems.treeDefinition import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        #final return is ignored because root has no previous node to return to
        _ = self.calculateMax(root) 

        return self.result

    def calculateMax(self, node):
        if not node:
            return 0
        
        leftMax = max(0, self.calculateMax(node.left))
        rightMax = max(0, self.calculateMax(node.right))

        # there can be only 1 split in a path
        self.result = max(self.result, node.val + leftMax + rightMax)
        
        # return without split
        return node.val + max(leftMax, rightMax)

