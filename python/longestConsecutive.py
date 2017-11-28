class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        unique = set(nums)
        for num in nums:
            # x in set: O(1)
            if not num - 1 in unique:
                new_length = 1
                cur = num
                while cur + 1 in unique:
                    cur += 1
                    new_length += 1
                length = max(length, new_length)
        
        return length