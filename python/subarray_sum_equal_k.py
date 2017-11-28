from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre = defaultdict(int)
        s = 0
        count = 0
        pre[0] = 1
        for i, num in enumerate(nums):
            s += num        
            count += pre[s - k]
            pre[s] += 1
                
        return count