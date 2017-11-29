# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque([])
        result = []
        order = collections.defaultdict(list)
        if root is None:
            return result
        queue.append((root, 0))
        while(queue):
            node, level = queue.popleft()
            if node:
                order[level].append(node.val)
                queue.append((node.left, level - 1))
                queue.append((node.right, level + 1))

        for i in sorted(order.keys()):
            result.append(order[i])

        return result
