"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checkSame(root1 : Optional[TreeNode] , root2 : Optional[TreeNode]) -> bool:
            if root1 == root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            

            left, right = checkSame(root1.left, root2.left), checkSame(root1.right, root2.right)

            if not left or not right:
                return False
            
            return root1.val == root2.val and left and right
        