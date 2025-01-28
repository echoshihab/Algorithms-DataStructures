"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of 
a binary tree and inorder is the inorder traversal of the same tree, construct and return the 
binary tree.

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


from typing import List, Optional

from Problems.treeDefinition import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 0th index is always root in preorder
        root = TreeNode(preorder[0]) 
        # find index of root in inorder
        mid = inorder.index(preorder[0]) 
        # recursively build left and right subtree by passing preorder and inorder array
        # of left and right subtree
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid]) # 

        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1: ])

        return root
