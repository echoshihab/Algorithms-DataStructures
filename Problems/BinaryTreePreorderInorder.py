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


import collections
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

class Solution2:
    def buildTree(self, preorder, inorder):
        #set up hashmap
        inorder_index_map = {}

        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i

        #set up deque so we can popleft from preorder items
        preorder = collections.deque(preorder)

        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder.popleft()
            root = TreeNode(root_val)
            root.left =  build(left, inorder_index_map[root_val] - 1)
            root.right  = build(inorder_index_map[root_val] + 1, right)

            return root
        
        return build(0, len(preorder) - 1)
            
