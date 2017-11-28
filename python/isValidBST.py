# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, None, None)
        
    def validBST(self, node, min_val, max_val):
        if node is None:
            return True
        if (min_val is not None) and node.val <= min_val:
            return False
        if (max_val is not None) and node.val >= max_val:
            return False
        
        leftvalid = True
        rightvalid = True
        if (node.left):
            leftvalid = self.validBST(node.left, min_val, node.val)
        if (node.right):
            rightvalid = self.validBST(node.right, node.val, max_val)
            
        return (leftvalid and rightvalid)