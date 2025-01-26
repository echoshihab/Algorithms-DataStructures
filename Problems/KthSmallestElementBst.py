"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

"""


import collections
from typing import Optional
from Problems.treeDefinition import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_queue = collections.deque()

        def k_arr_dfs(node):
            if node is None:
                return
            if not k_queue:
                k_queue.append(node.val)
            elif len(k_queue) < k:
                if k_queue[-1] > node.val:
                    k_queue.appendleft(node.val)
                else:
                    k_queue.append(node.val)
            elif k_queue[k-1] > node.val:
                k_queue.popleft()
                k_queue.append(node.val)
            k_arr_dfs(node.left)
            k_arr_dfs(node.right)

        k_arr_dfs(root)
        return k_queue[k-1]