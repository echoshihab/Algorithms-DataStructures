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
        if p == q == None:
            return True
        if p == None or q == None:
            return False
        
        left, right = self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)

        if not left or not right:
            return False
        
        return p.val == q.val and left and right
        
        