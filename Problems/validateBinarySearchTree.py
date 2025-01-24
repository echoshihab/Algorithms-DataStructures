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
        return self.validate(root, float("-inf"), float("inf"))

        
    def validate(self, node: Optional[TreeNode], left, right):

        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        

        return (self.validate(node.left, left, node.val) and
        self.validate(node.right, node.val, right))


        


        