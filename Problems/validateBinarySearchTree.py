"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


"""


from typing import Optional

from Problems.treeDefinition import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = right = True

        if root.left:
            if root.left.val < root.val:
                left = self.isValidBST(root.left)
            else:
                left = False
        else:
            left = True

            
        if root.right:
            if root.right.val > root.val:
                right = self.isValidBST(root.right)
            else:
                right = False
        else:
            right = True
        

        return left and right

        


        