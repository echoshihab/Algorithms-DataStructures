"""
Serialization is the process of converting a data structure or object into a sequence of
 bits so that it can be stored in a file or memory buffer, or transmitted across a network 
 connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction 
on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this 
string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a 
binary tree. You do not necessarily need to follow this format, so please be creative 
and come up with different approaches yourself.
"""

import collections

class TreeNode(object): 
    def __init__(self, x): 
        self.val = x 
        self.left = None 
        self.right = None 

#example Tree
class Codec:

    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque()
        queue.append(root)
        result = []


        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:                    
                    result.append(None)            
                    

        return str(result)



    def deserialize(self, data: str) -> TreeNode:
        pass


#example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
print(codec.serialize(root))