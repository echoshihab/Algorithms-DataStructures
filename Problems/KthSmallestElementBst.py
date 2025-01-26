"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

"""


from typing import Optional
from Problems.treeDefinition import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order_arr = []

        def inOrderDFS(node):
            if node is None:
                return
            inOrderDFS(node.left)
            in_order_arr.append(node.val)
            inOrderDFS(node.right)
        
        inOrderDFS(root)
        return in_order_arr[k-1]