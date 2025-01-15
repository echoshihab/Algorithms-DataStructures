"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
 you can see ordered from top to bottom.

 Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        result = []

        if root:
            queue.append(root)

        while queue:
            level_result = None

            for i in range(len(queue)):
                node = queue.popleft()
                
                level_result = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            result.append(level_result)

        return result
                    



        
        