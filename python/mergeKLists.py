# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        n = len(lists)
        curr = head
        pq = []
        idx = 0
        # idx is only for make the tuple can be sorted even when node.val same
        for node in lists:
            idx += 1
            if node:
                heapq.heappush(pq, (node.val, idx,  node))
        while(pq):
            curr.next = heapq.heappop(pq)[2]
            curr = curr.next
            if curr.next:
                idx += 1
                heapq.heappush(pq, (curr.next.val, idx, curr.next))

        return head.next
