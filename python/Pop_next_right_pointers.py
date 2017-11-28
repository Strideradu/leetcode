# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        cur = root
        level = None
        while cur.left:
            level = cur
            while(level):
                level.left.next = level.right
                if (level.next):
                    level.right.next = level.next.left
                level = level.next
            cur = cur.left

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur = root
        level = None

        while(cur):
            temp = TreeLinkNode(0)
            curChild = temp
            while(cur):
                if cur.left:
                    curChild.next = cur.left
                    curChild = curChild.next
                if cur.right:
                    curChild.next = cur.right
                    curChild = curChild.next
                cur = cur.next
            # right now temp.next = cur.left if cur has left child, or cur.right
            cur = temp.next
