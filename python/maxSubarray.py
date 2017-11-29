class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        s = 0
        for num in nums:
            if (s < 0):
                s = 0
            s += num            
                
            res = max(res, s)
            
        return res