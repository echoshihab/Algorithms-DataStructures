"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""


import collections
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
 
        level = 0
        calcDeque = collections.deque()
        calcDeque.append(root)
        

        while calcDeque:
            for i in range(len(calcDeque)):
                root = calcDeque.popleft()
                if root.left:
                    calcDeque.append(root.left)
                if root.right:
                    calcDeque.append(root.right)
            level += 1
            
        return level
    
    def iterativeDFS(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return max_depth






            
        