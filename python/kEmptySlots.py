class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        days = [0] * n
        for i in range(n):
            days[flowers[i] - 1] = i + 1
        left = 0
        right = k + 1
        res = float("inf")
        for i in range(n):
            if days[i] <= days[left] or days[i] <= days[right]:
                if i == right:
                    res = min(res, max(days[left], days[right]))
                left = i
                right = i + k + 1
                if right >= n:
                    break

        if res != float("inf"):
            return res
        else:
            return -1
