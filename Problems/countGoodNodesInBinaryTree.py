"""Given a binary tree root, a node X in the tree is named good if in the path from root
 to X there are no nodes with a value greater than X. Return the number of good nodes in the 
 binary tree.
 
 Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
 """


from Problems.binaryTreeRightSideView import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        def dfs(root, currMax):
            val_to_add = 0

            if root is None:
                return val_to_add

            if root.val >= currMax:
                val_to_add = 1
                currMax = root.val

            return val_to_add + dfs(root.left, currMax) + dfs(root.right, currMax)

        return dfs(root, root.val)
        