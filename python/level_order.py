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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        queue = collections.deque([])
        d = collections.defaultdict(list)
        queue.append((root, 0))
        result = []
        max_level = 0
        while queue:
            node, level = queue.popleft()
            if node:
                max_level = max(max_level, level)
                d[level].append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))

                if node.right:
                    queue.append((node.right, level + 1))

        for level in sorted(d.keys()):
            result.append(d[level])

        return result
