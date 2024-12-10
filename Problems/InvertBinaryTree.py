"""
Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n)        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = root
        self.invertSingleLevel(root)
        return dummy
            

    def invertSingleLevel(self, root):
        if root == None:
            return
        else:
            tempL = root.left
            tempR = root .right
            root.left = tempR
            root.right = tempL

            self.invertSingleLevel(root.left)
            self.invertSingleLevel(root.right)
            
            



        