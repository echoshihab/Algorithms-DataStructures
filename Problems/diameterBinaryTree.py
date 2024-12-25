"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


# big O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0


        def calculateDepth(node):
            if not node:
                return 0
            
            depth_left = calculateDepth(node.left)
            depth_right = calculateDepth(node.right)

            result = max(result, depth_left + depth_right)
            return 1 + max(depth_left, depth_right)
        
        calculateDepth(root)
        return self.result



        

        