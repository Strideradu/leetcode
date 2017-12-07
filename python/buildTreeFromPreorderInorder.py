# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        in_idx = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:in_idx + 1], inorder[0: in_idx])
        node.right = self.buildTree(
            preorder[in_idx + 1:], inorder[in_idx + 1:])
        return node
