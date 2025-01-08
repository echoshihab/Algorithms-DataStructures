"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to 
be a descendant of itself).

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
”"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # ensure p is smaller than q
        if p > q:        
            p,q = q,p

        # find node p and queue up node values
        queue = self.findNode(p)        

        self.result = None

        return self.findLCA(root, q, queue)
    
    def findLCA(self, root, node, queue):
        if node.val == root.val:
            return self.result

        if root.val != queue[0]:
            return self.result
        
        queue.pop(0)
        if node.val > root.val:
            return self.findLCA(node, root.right)
        
        return self.findLCA(node, root.left)
            

        # find node q and dequeue node values
        # if cannot dequeue, we have found the common denominator

    def findNode(self, root, node):
        queue = []

        queue.append(root.val)

        if node.val == root.val: return queue

        if node.val > root.val:
            return self.findNode(node, root.right)
        
        return self.findNode(node, root.left)




