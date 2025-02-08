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



class Codec:

    # O(n)
    def serialize(self, root):
        if not root:
            return ""
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

        
    # O(n)
    def deserialize(self, data):
        self.list_converted = collections.deque(data.split(","))  
        return self.dfs()

    def dfs(self):
        node_val = self.list_converted.popleft() # O(1)

        if not node_val:
            return

        root = TreeNode(node_val)
        root.left = self.dfs()
        root.right = self.dfs()

        return root
        
        
        



#example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
test = codec.serialize(root)
test2 = codec.deserialize(test)
test3 = codec.serialize(test2)

print(test3)