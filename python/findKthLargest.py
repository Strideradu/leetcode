class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = []
        right = []
        middle = []
        pivot = nums[0]
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)

            else:
                middle.append(num)
        r = len(right)
        m = len(middle)
        l = len(left)
        if l >= k:
            return self.findKthLargest(left, k)

        elif l + m >= k:
            return pivot
        else:
            return self.findKthLargest(right, k - m - l)


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        queue = []
        for num in nums:
            heapq.heappush(queue, num)
            if len(queue) > k:
                heapq.heappop(queue)

        return queue[0]  # or heapq.heappop(queue)
