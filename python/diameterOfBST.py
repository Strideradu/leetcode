# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdiameter = 0
        self._search(root)
        return self.maxdiameter

    def _search(self, root):
        if root is None:
            return -1

        r = self._search(root.right)
        l = self._search(root.left)
        self.maxdiameter = max(self.maxdiameter, 2 + r + l)

        return max(r, l) + 1
