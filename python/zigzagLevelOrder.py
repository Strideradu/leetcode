# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result

        queue = collections.deque([])
        queue.append((root, 0))
        d = collections.defaultdict(list)
        while(queue):
            node, level = queue.popleft()
            d[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        for i in range(len(d)):
            if i % 2 == 0:
                result.append(d[i][::1])
            else:
                result.append(d[i][::-1])

        return result
