# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while(cur):
            cur = cur.next
            count+=1
            if count == k:
                break
        
        if (count == k):
            succ = self.reverseKGroup(cur, k)
            prev = None
            cur = head
            while(cur):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                count -= 1
                if count == 0:
                    break
            head.next = succ
            head = prev
                
        return head