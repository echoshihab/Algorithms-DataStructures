"""
Given the roots of two binary trees root and subRoot, return true 
if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in 
tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSame(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False

            return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)

        if not root:
            return False
        if root.val == subRoot.val and checkSame(root, subRoot):
            return True

        left =  self.isSubtree(root.left, subRoot)           
        right = self.isSubtree(root.right, subRoot)

        if left or right:
            return True

        return False
 
            
            
            



        # check same
        