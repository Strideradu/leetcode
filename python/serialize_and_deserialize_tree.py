# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = ''
        if root is None:
            result += '#,'
            return result
        result += str(root.val) + ','
        result += self.serialize(root.left)
        result += self.serialize(root.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        sp = data[:-1].split(',')
        root, _ = self.deserializeHelper(sp, 0)
        return root

    def deserializeHelper(self, data, pos):
        if pos >= len(data) or data[pos] == '#':
            return None, pos + 1

        root = TreeNode(int(data[pos]))
        root.left, pos = self.deserializeHelper(data, pos + 1)
        root.right, pos = self.deserializeHelper(data, pos)

        return root, pos


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
