# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.max_path = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.max_path = root.val
        self.recursive(root)

        return self.max_path

    def recursive(self, node):
        if node is None:
            return 0
        l = self.recursive(node.left)
        r = self.recursive(node.right)
        self.max_path = max(self.max_path, node.val + l +
                            r, node.val + l, node.val + r)

        return max(node.val + l, node.val + r, node.val)
