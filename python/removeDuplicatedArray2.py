class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = collections.defaultdict(int)
        j = 0
        i = 0
        while i < len(nums) and j < len(nums):
            if freq[nums[i]] >= 2:
                i += 1
            else:
                nums[j] = nums[i]
                freq[nums[i]] += 1
                j += 1
                i += 1

        return j


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j
