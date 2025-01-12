"""Given the root of a binary tree, return the level order 
traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


from collections import defaultdict
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# first pass O(n + m)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.result = defaultdict(list)

        self.populateDict(root, 0)

        old_result = list(self.result.values())
        
        new_result = []
        while old_result:
            new_result.append(old_result.pop(0))
        
        return new_result
    
    def populateDict(self, root, currDepth):
        if not root:
            return 

        self.result[currDepth].append(root.val)

        self.populateDict(root.left, currDepth + 1)
        self.populateDict(root.right, currDepth + 1)


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        result = []
        queue = collections.deque()

        queue.append(root)

        while queue:
            currLevel = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    currLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if currLevel:
                result.append(currLevel)
        
        return result