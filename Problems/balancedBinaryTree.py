from typing import Optional

"""
Given a binary tree, determine if it is 
height-balanced (A height-balanced binary tree is a binary tree in which the depth of the two subtrees of
every node never differs by more than one.)

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n)        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True   
        calculateHeight(root)  

        def calculateHeight(root: Optional[TreeNode]): 
            if not root:
                return 0

            leftH  = calculateHeight(root.left)
            rightH = calculateHeight(root.right)

            if abs(leftH - rightH) > 1:
                self.result = False

            return 1 + max(leftH, rightH)
        
        return self.result

    def isBalanced2(self, root: Optional[TreeNode]) -> bool:

        def checkBalance(root):
            if root is None:
                return 0
            left = checkBalance(root.left)
            right = checkBalance(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return - 1

            return 1 + max(left, right)

        
        return checkBalance(root) != -1






