# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root != None:
            if root.left == None and root.right == None:
                depth = 1
            else:
                if root.left == None:
                    depth=self.maxDepth(root.right) + 1
                elif root.right == None:
                    depth=self.maxDepth(root.left) + 1
                else:
                    depth_left = self.maxDepth(root.left) + 1
                    depth_right = self.maxDepth(root.right) + 1
                    if depth_left > depth_right:
                        depth = depth_left
                    else:
                        depth = depth_right
        return depth