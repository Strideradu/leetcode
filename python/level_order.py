# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = defaultdict(list)
        self.dfs(root, level, 0)
        result = []
        for i in range(len(level)):
            result.append(level[i])

        return result

    def dfs(self, node, level, lv):
        if node is None:
            return
        level[lv].append(node.val)
        self.dfs(node.left, level, lv + 1)
        self.dfs(node.right, level, lv + 1)
