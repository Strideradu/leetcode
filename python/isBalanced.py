# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.balance = True
        self.depth(root)
        return self.balance

    def depth(self, node):
        if node is None:
            return 0

        leftDepth = self.depth(node.left)
        rightDepth = self.depth(node.right)

        max_depth = max(leftDepth, rightDepth)
        min_depth = min(leftDepth, rightDepth)
        if max_depth - min_depth > 1:
            self.balance = False

        return max_depth + 1
